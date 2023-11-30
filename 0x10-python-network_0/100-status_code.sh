#!/bin/bash
# script that displays only the status code without using pipe
curl -s -o /dev/null -w "%{http_code}" "$1"
