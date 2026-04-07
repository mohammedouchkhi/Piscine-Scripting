#!/bin/bash

# $1 captures the first argument (the file path) passed to the script
if [ -x "$1" ]; then
  echo "File is executable"
else
  echo "File is not an executable or does not exist"
fi