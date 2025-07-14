#!/usr/bin/env python3

import requests
import logging
from datetime import datetime
import pytz
import os
import sys

list_of_websites = [
    'google.com',
    'github.com',    
]

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# put the list of website in a file with this name website_list.txt
file_name = 'website_list.txt'
if os.path.isfile(file_name):
    with open(file_name, 'r') as file:
        list_of_websites = [line.strip() for line in file if line.strip()]  # Load websites, stripping whitespace
else:
    print(f"{file_name} does not exist. Please create the file with a list of websites.")
    exit(1) 

scheme = 'https://'

# Define the timezone
log_tz = pytz.timezone('Asia/Tehran')

# Configure logging
logging.basicConfig(filename='website_status.log', level=logging.INFO, format='%(asctime)s - %(message)s')

all_sites_checked = True

for item in list_of_websites:    
    try:
        response = requests.get(f"{scheme}{item}", timeout=3)
        if response.status_code == 200:
            print(".", end="")
        else:
            print("f", end="")            
            # Log the status
            logging.info(f"{item} is not live. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("F", end="")
        all_sites_checked = False
        # print(item, " : is not live")
        # Log the exception with a timestamp
        logging.info(f"{item} is not live. Error: {str(e)}")

if all_sites_checked:
    print(' All site is checked, see the log file')
else: 
    print(' Some website could not be checked')
    
# To ensure the log entries have the correct timezone
for handler in logging.getLogger().handlers:
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))