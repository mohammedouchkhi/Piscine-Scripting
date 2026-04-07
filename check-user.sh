#!/bin/bash

if [[ $# -ne 2 ]]; then
  >&2 echo "Error: expect 2 arguments"
  exit 1
fi

flag="$1"
username="$2"

user_info=$(getent passwd "$username")

if [[ "$flag" == "-e" ]]; then
  if [[ -n "$user_info" ]]; then
    echo "yes"
  fi

elif [[ "$flag" == "-i" ]]; then
  if [[ -n "$user_info" ]]; then
    echo "$user_info"
  fi

else
  >&2 echo "Error: unknown flag"
  exit 1
fi
