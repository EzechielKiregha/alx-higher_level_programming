#!/bin/bash
# a script that sends a delete request to a given url and return the response body
curl -sX DELETE "$1"
