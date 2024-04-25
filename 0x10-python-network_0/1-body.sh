#!/bin/bash
# takes in a URL, sends a GET request, displays only body of a 200 status code response
curl -s -L "${1}"
