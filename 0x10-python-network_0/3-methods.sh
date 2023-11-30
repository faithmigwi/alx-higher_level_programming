#!/bin/bash
# script takes in a URL and displays all HTTP methods the server will accept
curl -s -I "$1" | grep Allow | sed 's/^Allow: //'
