#!/usr/bin/env bash

source setup_env.sh

env_name="test_project1"
create_env $env_name

install_modules nltk nltk_tgrep

run "-m unittest discover -s constituent_counter"

cleanup_env $env_name