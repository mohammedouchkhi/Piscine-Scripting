#!/bin/bash

# Define the operation functions
do_add() {
  echo $(($1 + $2))
}

do_sub() {
  echo $(($1 - $2))
}

do_mult() {
  echo $(($1 * $2))
}

do_divide() {
  echo $(($1 / $2))
}

# 1. Check for the correct number of arguments
if [ "$#" -ne 3 ]; then
  >&2 echo "Error: expect 3 arguments"
  exit 1
fi

# 2. Check if the first and third arguments are valid numbers (including negative)
if [[ ! "$1" =~ ^-?[0-9]+$ ]] || [[ ! "$3" =~ ^-?[0-9]+$ ]]; then
  >&2 echo "Error: invalid number"
  exit 4
fi

# 3. Check for division by zero
if [ "$2" = "/" ] && [ "$3" -eq 0 ]; then
  >&2 echo "Error: division by 0"
  exit 2
fi

# 4. Use a case statement to select the correct operator and call the function
case "$2" in
  "+")
    do_add "$1" "$3"
    ;;
  "-")
    do_sub "$1" "$3"
    ;;
  "*")
    do_mult "$1" "$3"
    ;;
  "/")
    do_divide "$1" "$3"
    ;;
  *)
    # If the operator doesn't match the four valid choices
    >&2 echo "Error: invalid operator"
    exit 3
    ;;
esac
