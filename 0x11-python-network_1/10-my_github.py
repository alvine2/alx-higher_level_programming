#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py:")
        sys.exit(1)
    
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")

