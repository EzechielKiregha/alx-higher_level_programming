#!/bin/bash
#this script sends a post request to an endpoint using curl while setting the body using variables
curl -X POST -d "email='test@gmail.com'&subject='I will always be here for PLD'" -s "$1"
