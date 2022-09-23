#!/bin/bash
# takes a url, send request and display size of body
curl -sI "$1" | grep Content-Length | cut -d " " -f2

