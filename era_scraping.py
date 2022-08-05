# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 00:01:44 2022

Description:
    - simple web scraping script to download files from the SEC website

@author: Laci
"""

import urllib
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Information About Registered Investment Advisers and Exempt Reporting Advisers
url = 'https://www.sec.gov/help/foiadocsinvafoiahtm.html'

# SEC website, we'll download zip files from here
base_url = 'https://www.sec.gov'

# connect to url
r = requests.get(url)

# read the webpage
soup = BeautifulSoup(r.text, 'html.parser')

# read everything that is in a table and has a link
target_links = [base_url + tag.find("a")["href"] for tag in soup.select("td:has(a)")]


# download every zip file from the links
for index, t in enumerate(target_links):
    print(f'{index}/{len(target_links)}', t)
    
    # new name of the file, numbers only
    new_name = t.split('/')[-1]
    
    # downloading the files into a data folder
    local_filename = urllib.request.urlretrieve(t, filename=f'data/{new_name}')
    
    
# read table where all the links are found
table = pd.read_html(url)[0]

# insert the links to a new column
table['names'] = target_links

# filenames - split the string on '/' and get the last element of the list
table['files'] = table['names'].apply(lambda x: x.split('/')[-1])

# export to .csv
table.to_csv('DETAILS.csv', sep=';', index=False)


