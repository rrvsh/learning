{ pkgs, ... }:
{
  languages.python = {
    enable = true;
    venv.enable = true;
    venv.requirements = ''
      win2xcur
    '';
  };
  packages = [
    pkgs.python312Packages.wand
  ];
}
