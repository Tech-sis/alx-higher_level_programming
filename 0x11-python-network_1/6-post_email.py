#!/usr/bin/python3
"""
Send a post request to a given url with
a given email using the requests module
"""
import sys
import requests

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
