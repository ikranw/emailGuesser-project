# email_guesser.py

import re
import requests
from bs4 import BeautifulSoup
import time
import random
import csv

# Colours
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[39m"

class NameType(Exception):
    pass

#collects user inputs and checks if they meet the data types it should be. 
def collect_user_input():
    name_input = input(yellow + 'Please enter name: ' + reset)
    if not name_input.isalpha():
        raise ValueError("Name must be alphabetic characters only.")

    last_name_input = input(yellow + "Please enter surname: " + reset)
    if not last_name_input.isalpha():
        raise ValueError("Surname must be alphabetic characters only.")

    birth_input = input(yellow + "Please enter birth year (or no): " + reset)

    username_input = input(yellow + "Please enter username (or no): " + reset)

    skype_input = input(yellow + "Would you like to automatically add to the pool Skype usernames from people using this name in Skype? (y/n) " + reset)
    while skype_input != "y" and skype_input != "n":
        print(red + "Please input 'y' or 'n'!" + reset)
        skype_input = input(yellow + "Would you like to automatically add to the pool Skype usernames from people using this name in Skype? (y/n) " + reset)

    extra_formats_input = input(yellow + "Would you like to add more e-mail formats apart from the preconfigured ones? (y/n) " + reset)
    while extra_formats_input != "y" and extra_formats_input != "n":
        print(red + "Please select a valid input." + reset)
        extra_formats_input = input(yellow + "Would you like to add more combinations than the preconfigured ones? (y/n) " + reset)

    extra_formats = []
    if extra_formats_input == "y":
        extra_formats = input(yellow + "Provide all extra formats you wish to examine, separated by commas: " + reset).split(",")

    domain = []
    while not domain:
        domain = input(yellow + "Please enter domains separated by a single comma: " + reset).split(",")
        if not domain:
            print(red + "You must input at least one domain to be searched!" + reset)

    return name_input, last_name_input, birth_input, username_input, skype_input, domain, extra_formats



"""function to generate_emails combinations"""
def generate_emails(name_input, last_name_input, birth_input, username_input, skype_input, domain, extra_formats):
    # Generate email combinations
    emails = []
    for dom in domain:
        structure = ["first!!", "f!!last!!", "f!!_last!!", "last!!f!!", "last!!_f!!", "first!!.last!!", "first!!_last!!", "last!!.first!!", "last!!_first!!"]

        if extra_formats:
            structure.extend(extra_formats)

        if birth_input != "no":
            structure.extend([
                "last!!first!!" + birth_input,
                "first!!last!!" + birth_input,
                "f!!last!!" + birth_input,
                "f!!_last!!" + birth_input,
                "first!!.last!!" + birth_input,
                "first!!_last!!" + birth_input,
                "last!!.first!!" + birth_input,
                "last!!_first!!" + birth_input,
                "first!!last!!" + birth_input[2:],
                "last!!first!!" + birth_input[2:],
                "f!!last!!" + birth_input[2:],
                "f!!_last!!" + birth_input[2:],
                "first!!.last!!" + birth_input[2:],
                "first!!_last!!" + birth_input[2:],
                "last!!.first!!" + birth_input[2:],
                "last!!_first!!" + birth_input[2:],
                "first!!last!!." + birth_input,
                "first!!.last!!." + birth_input,
                "f!!last!!." + birth_input,
                "f!!_last!!." + birth_input,
                "first!!.last!!." + birth_input,
                "first!!_last!!." + birth_input,
                "last!!.first!!." + birth_input,
                "last!!_first!!." + birth_input,
                "first!!last!!_" + birth_input,
                "first!!.last!!_" + birth_input,
                "f!!last!!_" + birth_input,
                "f!!_last!!_" + birth_input,
                "first!!.last!!_" + birth_input,
                "first!!_last!!_" + birth_input,
                "last!!.first!!_" + birth_input,
                "last!!_first!!_" + birth_input,
                "first!!last!!." + birth_input[2:],
                "first!!.last!!." + birth_input[2:],
                "f!!last!!." + birth_input[2:],
                "f!!_last!!." + birth_input[2:],
                "first!!.last!!." + birth_input[2:],
                "first!!_last!!." + birth_input[2:],
                "last!!.first!!." + birth_input[2:],
                "last!!_first!!." + birth_input[2:],
                "first!!last!!_" + birth_input[2:],
                "first!!.last!!_" + birth_input[2:],
                "f!!last!!_" + birth_input[2:],
                "f!!_last!!_" + birth_input[2:],
                "first!!.last!!_" + birth_input[2:],
                "first!!_last!!_" + birth_input[2:],
                "last!!.first!!_" + birth_input[2:],
                "last!!_first!!_" + birth_input[2:]
            ])

        if username_input != "no":
            structure.append(username_input)
            if birth_input != "no":
                structure.extend([
                    username_input + birth_input,
                    username_input + birth_input[2:],
                    username_input + "." + birth_input,
                    username_input + "_" + birth_input,
                    username_input + "." + birth_input[2:],
                    username_input + "_" + birth_input[2:]
                ])

        for x in structure:
            x = x.replace("first!!", name_input)
            x = x.replace("last!!", last_name_input)
            x = x.replace("f!!", name_input[0])
            x = x.replace("l!!", last_name_input[0])
            emails.append(x + "@" + dom)

    return emails

def verify_emails(emails):
    # Verify email syntax
   regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
   verified_emails = []
    for email in emails:
        match = re.match(regex, email)
        if match:
            verified_emails.append(email)
    return verified_emails

def main():
    try:
        print("Welcome to " + green + "emailGuesser" + reset + "!")
        print("Developed by " + blue + "White Hat Inspector (@WHInspector)" + reset + ".")
        print("For feedback and/or questions send me a private message on " + blue + "https://twitter.com/whinspector" + reset)
        print("")

        # Collect user input function
        name_input, last_name_input, birth_input, username_input, skype_input, domain, extra_formats = collect_user_input()

        # Generate emails
        emails = generate_emails(name_input, last_name_input, birth_input, username_input, skype_input, domain, extra_formats)


if __name__ == "__main__":
    main()
