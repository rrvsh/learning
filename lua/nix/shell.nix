{ pkgs }:
pkgs.mkShell {
  buildInputs = with pkgs; [ lua ];
}
