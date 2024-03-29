#!/bin/bash
# bash script for code_status
curl -s -o /dev/null -w "%{http_code}" "$1"
