#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = data.encode('utf8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf8'))
