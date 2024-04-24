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


""" function to implement the contribution and feauture of "Allow users to parse a preconfigured .txt file with 
email formats or/and domains, so that they can automatically
input the same preferences every time they run a search, 
without having to manually input the same things each time" """

def parse_email_formats(filename):
    # Parse the preconfigured .txt file for email formats or domains
    formats = []
    domains = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '@' in line:
                formats.append(line)
            else:
                domains.extend(line.split(','))
    return formats, domains


def main():
    try:
        # Parse preconfigured file
        email_formats, domain = parse_email_formats("preconfigured.txt")

if __name__ == "__main__":
    main()
