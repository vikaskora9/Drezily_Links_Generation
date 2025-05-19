import json
import math
import time
import traceback
from bs4 import BeautifulSoup
import os
import numpy as np
import pandas as pd
import requests
import pymongo
df, ctr = pd.DataFrame(), 0
with open('home.html', "r", encoding="utf-8") as file:
        html_content = file.read()
        prod_data = BeautifulSoup(html_content, 'html.parser')
        for url in prod_data.find('nav', {'aria-labelledby':'side-sub-nav-4'}).find_all('li'):
            # print(url.find('a')['href'])
            resp = json.loads(requests.get(f"https://www.revolve.com/content/nav/visual/search?offset=0&limit=500&currentUrl=https%3A%2F%2Fwww.revolve.com{url.find('a')['href']}&includeDisabledFilters=true&category=dresses",
                                                                 headers={
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
                                            'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
}).text)
            df.at[ctr, 'Name'] = url.text.strip()
            df.at[ctr, 'Total'] = resp['total']
            ctr += 1

df.to_csv('Revolve_By_Style.csv', index=False, index_label=False)