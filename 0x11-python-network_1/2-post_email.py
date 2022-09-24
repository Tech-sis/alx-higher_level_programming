#!/usr/bin/python3
"""
Take in a URL, send a POST request,
and display the body of response
(decoded in utf-8).
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
