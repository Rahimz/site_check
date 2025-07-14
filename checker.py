import requests
import logging
from datetime import datetime
import pytz
import os

list_of_websites = [
    'google.com',
    'github.com',    
]

# put the list of website in a file with this name website_list.txt
file_name = 'website_list.txt'
if os.path.isfile(file_name):
    with open(file_name, 'r') as file:
        list_of_websites = [line.strip() for line in file if line.strip()]  # Load websites, stripping whitespace


scheme = 'https://'

# Define the timezone
tehran_tz = pytz.timezone('Asia/Tehran')

# Configure logging
logging.basicConfig(filename='website_status.log', level=logging.INFO, format='%(asctime)s - %(message)s')


for item in list_of_websites:
    try:
        response = requests.get(f"{scheme}{item}")
        if response.status_code == 200:
            print(item, " : is live")
        else:
            print(item, " : is not live")
            # Log the status
            logging.info(f"{item} is not live. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(item, " : is not live")
        # Log the exception with a timestamp
        logging.info(f"{item} is not live. Error: {str(e)}")

# To ensure the log entries have the correct timezone
for handler in logging.getLogger().handlers:
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))