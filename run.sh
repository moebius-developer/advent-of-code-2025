#!/usr/bin/env bash

run() {
  local this_dir
  this_dir="$(dirname "$(readlink --canonicalize --verbose "$BASH_SOURCE")")" || exit

  local direc=''
  for direc in $(/bin/ls --directory day*); do
    "$direc/solution1.py"
    "$direc/solution2.py"
  done
}

set -o errexit
set -o pipefail
set -o nounset
run "$@"
