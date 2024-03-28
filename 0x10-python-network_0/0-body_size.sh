#!/bin/bash
[ $# -ne 1 ] && { echo "Usage: $0 URL"; exit 1; }
curl -s -o /dev/null -w "%{size_download}\n" "$1"

