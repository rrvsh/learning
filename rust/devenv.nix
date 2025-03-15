{pkgs, ...}: {
  languages.rust = {
    enable = true;
    channel = "nixpkgs";
  };

  packages = with pkgs; [
    rustlings
  ];
}
