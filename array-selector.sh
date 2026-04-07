#!/bin/bash

colors=("red" "blue" "green" "white" "black")
if [[ $# -ne 1 ]] || [[ ! $1 =~ ^[0-9]+$ ]] || [[ $1 -lt 1 ]] || [[ $1 -gt ${#colors[@]} ]]; then
  echo "Error"
else
  index=$(($1 - 1))
  echo "${colors[$index]}"
fi
