{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.flask
  ];

  shellHook = ''
    echo "Environment ready. Python and Flask have been installed."
  '';
}
