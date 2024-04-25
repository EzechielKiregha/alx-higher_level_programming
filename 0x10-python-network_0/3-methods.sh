#!/bin/bash
# a script that prints out all the methods that the server accepts
curl -sX OPTIONS "$1"
