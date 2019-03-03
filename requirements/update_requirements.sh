#!/usr/bin/env bash

echo "updating development packages"
pip-compile --output-file dev.txt dev.in --upgrade
