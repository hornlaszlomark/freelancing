# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 00:03:18 2022

@author: Laci
"""

import urllib
import pandas as pd

# exemptions in 2022 June 
f = 'ia060122-exempt.csv'

# read csv file
df = pd.read_csv(f, sep=',')

# get CRD number
crd = df['Organization CRD#'].unique()

# download pdf files from SEC website          
for number in crd:
    
    # the SEC website is checking for header, otherwise your request gets denied
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'whatever')
    
    # pdf link
    pdf_url = f'https://reports.adviserinfo.sec.gov/reports/ADV/{number}/PDF/{number}.pdf'
    
    # download
    filename, headers = opener.retrieve(pdf_url, filename=f'C:/Python/FREELANCING/exempt_record_advisers/2022-06/{number}.pdf')
    
