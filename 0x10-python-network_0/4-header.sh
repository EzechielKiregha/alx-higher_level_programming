#!/bin/bash
#a script that sends a get request to and endpoint with an header variable
curl -H "X-School-User-Id: 98" "${1}"
