#!/usr/bin/env bash
set -euo pipefail

contains=0
overlaps=0
while read -r line; do
    declare -a range1=( $(echo $line | cut -d, -f1 | tr '-' '\n') )
    declare -a range2=( $(echo $line | cut -d, -f2 | tr '-' '\n') )

    if ([[ "${range1[0]}" -le "${range2[0]}" ]] && [[ "${range1[1]}" -ge "${range2[1]}" ]]) \
            || ([[ "${range1[0]}" -ge "${range2[0]}" ]] && [[ "${range1[1]}" -le "${range2[1]}" ]]); then
        contains=$((contains+1))
    fi

    if [[ $(comm -12 <( seq ${range1[0]} ${range1[1]} | sort ) <( seq ${range2[0]} ${range2[1]} | sort )) ]]; then
        overlaps=$((overlaps+1))
    fi
done < input.txt

echo "Part 1: $contains"
echo "Part 2: $overlaps"
