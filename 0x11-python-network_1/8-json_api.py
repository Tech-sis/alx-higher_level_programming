#!/usr/bin/python3
"""
sends a post request with a letter as a parameter
"""
import json
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg: ""
    payload = {'q': arg}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)
    try:
        r.raise_for_status()
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception as e:
        print("Not a valid JSON")
