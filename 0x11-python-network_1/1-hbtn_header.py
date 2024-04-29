#!/usr/bin/python3
'''
This Script that fetches https://alx-intranet.hbtn.io/status
using the urllib package.
'''
from urllib import request
import sys

if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
