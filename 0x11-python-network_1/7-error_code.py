#!/usr/bin/python3
"""
Use a package to send a request
to a URL and display the body of
the response, or error code if the
request fails.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
