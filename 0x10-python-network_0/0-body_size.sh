#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

# Send request to URL and store response in a temporary file
response=$(mktemp)
curl -s -o "$response" "$url"

# Get the size of the response body in bytes
size=$(wc -c < "$response")

# Display the size of the response body
echo "$size"

# Clean up temporary file
rm "$response"
