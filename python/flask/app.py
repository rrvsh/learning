from flask import (
    Flask,
    render_template,
    render_template_string,
    request,
    session,
    redirect,
    url_for,
)
from markupsafe import escape

app = Flask(__name__)


@app.get("/")
def home():
    return "home"


@app.route("/hello/")
@app.route("/hello/<username>")
def hello(username=None):
    return render_template("hello.html", person=username)


# Thanks to https://testdriven.io/blog/flask-sessions/

# Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
app.secret_key = "BAD_SECRET_KEY"


@app.route("/set_email", methods=["GET", "POST"])
def set_email():
    if request.method == "POST":
        # Save the form data to the session object
        session["email"] = request.form["email_address"]
        return redirect(url_for("get_email"))

    return """
        <form method="post">
            <label for="email">Enter your email address:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Submit</button
        </form>
        """


@app.route("/get_email")
def get_email():
    return render_template_string(
        """
            {% if session['email'] %}
                <h1>Welcome {{ session['email'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
        """
    )


@app.route("/delete_email")
def delete_email():
    # Clear the email stored in the session object
    session.pop("email", default=None)
    return "<h1>Session deleted!</h1>"
