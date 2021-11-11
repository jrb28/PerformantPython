# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:59:48 2021

@author: james
"""

import requests

with open('files/fips_state_codes.csv', 'r') as f:
    state_codes = f.readlines()
    
state_codes = [line.strip().split(',') for line in state_codes]
state_codes = [(state, abbrv, code.zfill(2)) for state, abbrv, code in state_codes]

key = '902172a1c340398d9458b24ce69b87d28ce086c0'
print_success = False

while not print_success:
    start = True
    error = False

    for state, abbrv, code in state_codes:
        print(state, abbrv, code)
        url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=tract:*&in=state:{code}&key={key}'
        response = requests.get(url, 
                                headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
        while response.status_code == 500:
            #print('Internal Server Error')
            #error = True
            #break
            print(state, abbrv, code)
            response = requests.get(url, 
                                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
        if response.status_code != 204:
            response = response.json()
        
            if len(response) > 0:
                if start:
                    result = response
                else:
                    result += response[1:]
                start = False
         
            
    if not error:
        with open('files/tract_codes.csv', 'w', encoding='utf8') as f:
            f.write('\n'.join([','.join(line) for line in result]).rstrip())
        print_success = True