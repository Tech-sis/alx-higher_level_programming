#!/bin/bash
# displays methods
curl -sI "$1" | grep Allow | cut -d " " -f2-
