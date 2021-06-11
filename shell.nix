# shell.nix
with (import <nixpkgs> {});

mkShell {
  buildInputs = [
    python3Packages.python
    python3Packages.tkinter
    python3Packages.pandas
    python3Packages.matplotlib
    python3Packages.yfinance
    ripgrep
  ];
}
