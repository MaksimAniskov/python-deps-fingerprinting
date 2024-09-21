#!/bin/sh
stdout_to_file="$1"
shift 1
python /usr/src/stat_analysis.py "$@" >"$stdout_to_file"
