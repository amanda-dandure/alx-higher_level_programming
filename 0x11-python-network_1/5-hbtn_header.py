#!/usr/bin/python3
"""Displaying the X-Request-Id header var of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
