#!/usr/bin/python3
"""Take in a url, send a request to the URL and display the value of `X-Request-Id` variable found in the header of the response."""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
