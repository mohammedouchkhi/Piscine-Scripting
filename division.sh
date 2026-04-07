#!/bin/bash

# Check if fewer than two arguments are provided
if [[ $# -lt 2 ]]; then
  echo "Error: two numbers must be provided"
  exit 1
fi

# Check if either argument is NOT a valid integer (using a regular expression)
if [[ ! $1 =~ ^-?[0-9]+$ ]] || [[ ! $2 =~ ^-?[0-9]+$ ]]; then
  echo "Error: both arguments must be integers"
  exit 1
fi

# Check if the divisor is 0 (or multiple zeros like 00, -0)
if [[ $2 =~ ^-?0+$ ]]; then
  echo "Error: division by zero is not allowed"
  exit 1
fi

# Perform the division using bc for arbitrary precision
echo "$1 / $2" | bc