for n in range(100):
    numberToEvaluate = n + 1
    buffer = ""
    if numberToEvaluate % 3 == 0:
        buffer += "Fizz"
    if numberToEvaluate % 5 == 0:
        buffer += "Buzz"
    if buffer == "":
        print numberToEvaluate
    else:
        print buffer
