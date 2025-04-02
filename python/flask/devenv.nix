{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = ''
        flask
      '';
    };
  };
  processes = {
    flask-run.exec = "flask run --host=0.0.0.0 --debug";
  };
}
