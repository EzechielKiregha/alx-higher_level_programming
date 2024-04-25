#!/bin/bash

# a script that gets the total number of bytes of a response body when using curl
curl -s $1 | wc -c

# # Check if URL argument is provided
# if [ -z "$1" ]; then
#     echo "Usage: $0 URL"
#     exit 1
# fi

# url=$1

# # Send request to URL and get the size of the response body in bytes
# size=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# # Display the size of the response body
# echo "$size"
