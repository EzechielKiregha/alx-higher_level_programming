#!/bin/bash
# a script that gets the total number of bytes of a response body when using curl
curl -s $1 | wc -c
