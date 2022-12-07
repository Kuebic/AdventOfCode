#!/bin/bash

INPUT="./test.txt"

test=$(head -n 1 "$INPUT")

echo $test

counter=0
for i in $(sed -r 's?(.)?\1 ?g' $INPUT); do
  signal[$counter]=$i
  counter=$(($counter+1))
done

echo $test
echo $counter
