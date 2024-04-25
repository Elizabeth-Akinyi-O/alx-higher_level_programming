#!/bin/bash
# Sends a request to a URL passed as an argument. You can't use any pipe, redirection, ; and &&
curl -so /dev/null -w "%{http_code}" "$1"
