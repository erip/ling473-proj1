#!/usr/bin/env bash

source /usr/bin/virtualenvwrapper.sh

function create_env() {
  echo "Creating virtualenv $1..."
  mkvirtualenv -p /bin/python3 "$1" >/dev/null 2>&1
}

function install_modules() {
  echo "Installing necessary packages..."
  pip3 install "$@" >/dev/null 2>&1

  echo "Installed:"
  pip3 freeze
}

function run() {
  echo "Running $1..."
  /usr/bin/env python3 $1
}

function cleanup_env() {
  echo "Removing virtualenv $1"
  deactivate && rmvirtualenv "$1" >/dev/null 2>&1
}
