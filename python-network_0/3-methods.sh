#!/bin/bash
<<<<<<< HEAD
# takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
=======
# display all HTTP methods the server will accept using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
>>>>>>> 27c8e46bdfc3f080d57d5a6b14fd0aada149cd93
