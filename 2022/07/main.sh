#!/bin/bash

top_dir=$(pwd)

rm -rf "${top_dir}/scratch"
mkdir "${top_dir}/scratch"
cd "${top_dir}/scratch"

while read line; do
  set $line
  if [[ "$2" = "cd" ]]; then
    if [[ "$3" = "/" ]]; then
      cmd="cd ${top_dir}/scratch";
    else
      cmd="cd $3";
    fi
  elif [[ "$2" = "ls" ]]; then
    cmd="";
  elif [[ "$1" = "dir" ]]; then
    cmd="mkdir $2";
  else
    cmd="dd if=/dev/zero of=$2 bs=$1 seek=1 count=0"
  fi
  eval "$cmd" > /dev/null 2>/dev/null
done < "${top_dir}/test.txt"

# find $top_dir/scratch/ -type d -print0 | xargs -0 -I{.} find {.} -type f -exec du -cb {} + | grep total | awk '{ if ($1 <= 100000) { s += $1 } } END {print s}'

# TOTAL_FILESIZE="$(find scratch/ -type f -exec du -cb {} + | grep total | cut -f1)"
# find $top_dir/scratch/ -type d -print0 | xargs -0 -I{.} find {.} -type f -exec du -cb {} + | grep total | sort -n | awk "{ if ($TOTAL_FILESIZE - \$1 <= 40000000) { print \$1; exit; } }"
