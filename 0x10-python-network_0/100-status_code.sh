#!/bin/bash
# sends a get request to a given url and displays responce status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
