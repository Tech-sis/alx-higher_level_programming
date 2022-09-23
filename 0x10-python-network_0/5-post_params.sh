#!/bin/bash
# sends a post request
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be there for PLD"
