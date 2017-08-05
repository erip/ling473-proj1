#!/usr/bin/env bash

source setup_env.sh

env_name="project1"
create_env $env_name

install_modules nltk nltk_tgrep

run ./main.py

cleanup_env $env_name
