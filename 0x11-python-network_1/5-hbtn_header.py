#!/usr/bin/python3
"""
sends a request to the URL and
displays the value of the
X-Request-Id using requests package
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
