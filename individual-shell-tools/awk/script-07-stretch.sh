#!/bin/bash

set -euo pipefail

awk '{
  if (!seen[$1]) { order[++count] = $1; seen[$1] = 1 }
  for (i=3; i<=NF; i++) sum[$1] += $i
} END {
  for (i=1; i<=count; i++) print order[i], sum[order[i]]
}' scores-table.txt

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output just the names of each player along with the total of adding all of that player's scores.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 15". The second line should be "Basia 37"
