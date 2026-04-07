#!/bin/bash

if [[ $# -ne 1 ]] || [[ ! "$1" =~ ^[0-9]+$ ]] || [[ "$1" -lt 1 ]] || [[ "$1" -gt 100 ]]; then
  echo "Error: wrong argument"
  exit 1
fi

secret=$1
moves=1

for (( tries=5; tries>0; )); do
  echo "Enter your guess ($tries tries left):"
  read guess
  
  if [[ -z "$guess" ]] || [[ ! "$guess" =~ ^[0-9]+$ ]] || [[ "$guess" -lt 1 ]] || [[ "$guess" -gt 100 ]]; then
    continue
  fi
  
  if [[ "$guess" -gt "$secret" ]]; then
    echo "Go down"
  elif [[ "$guess" -lt "$secret" ]]; then
    echo "Go up"
  else
    echo "Congratulations, you found the number in $moves moves!"
    exit 0
  fi
  
  ((tries--))
  ((moves++))
done

# if the loop finishes without exiting, the player ran out of tries
echo "You lost, the number was $secret"
