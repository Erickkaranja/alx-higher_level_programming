#!/bin/bash
# sends a JSON POST request to a URL passed as first arguement.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
