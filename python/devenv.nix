{ pkgs, ... }:
{
  languages.python = {
    enable = true;
    version = "3.9";
    venv.enable = true;
    venv.requirements = ''
      win2xcur
    '';
  };
  packages = [
    pkgs.python39Packages.wand
  ];
}
