#!/bin/bash
# Bash script returns all acceted methods.
curl -sI "$1" | grep "allow" | cut -d " " -f 2-
