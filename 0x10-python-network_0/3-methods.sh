#!/bin/bash
# bash script
curl -sI OPTIONS "$1" | grep -i "^Allow" | cut -d " " -f 2-
