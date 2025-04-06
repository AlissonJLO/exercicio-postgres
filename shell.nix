{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.virtualenv
    pkgs.zlib
    pkgs.stdenv.cc.cc.lib
    pkgs.docker
    pkgs.docker-compose
  ];

  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH
    export VENV=.venv
    if [ ! -d $VENV ]; then
      python -m venv $VENV
      source $VENV/bin/activate
      pip install -r requirements.txt
    else
      source $VENV/bin/activate
    fi

    export PYTHONPATH=$PWD:$PYTHONPATH
    echo "Ambiente Nix ativado com sucesso."
    echo "Use 'docker-compose up -d' para iniciar o banco de dados PostgreSQL."
  '';
}
