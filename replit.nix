{pkgs}: {
  deps = [
    pkgs.python312Packages.pymongo
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.python312Packages.flask
  ];
}
