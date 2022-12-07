#!/bin/bash

# Read the input signal from a file
signal=$(cat input.txt)

# Define the function to solve the problem
function solve {
  # Loop through each character in the signal
  for (( i=$1; i<${#signal}; i++ )); do
    # Extract the substring of the specified length
    s=${signal:i-$1:$1}
    # Check if the substring contains only unique characters
    if [[ $(echo $s | grep -o . | sort | uniq | wc -l) == $1 ]]; then
      # Print the index and exit the loop
      echo $i
      break
    fi
  done
}

# Call the function with the given marker lengths
solve 4
solve 14
