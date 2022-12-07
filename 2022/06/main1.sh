#!/bin/bash

input=$1
k=0
for i in  $(sed -r 's?(.)?\1 ?g' $input); do
  signal[$k]=$i
  k=$(($k+1))
done

function solve () {
  for i in $(seq 0 $(($k-$1))); do
    echo $(seq $i $($i+$(($1-1))))
    for g in $(seq $i $($i+$(($1-1)))); do
      echo $i $g
      echo  ${signal[$g]}
    done | sort | uniq | wc -l | grep -q "^${1}$" && { echo $(($i+$1)); break; }
  done
}

solve 4
