#!/bin/bash
#takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. Set header variable X-HolbertonSchool-User-Id  with value 98"
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
