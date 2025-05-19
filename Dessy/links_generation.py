import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

resp = json.loads(requests.get('https://dyn.dessy.com/api/fastnav/parseUrl/?countrycode=us&currencycode=USD&addbuckets=displaydessyus&url=%2Fbridesmaid-dresses%2F%3Fpage%3D2%26rpp%3D36').text)
# print(resp)
df = pd.DataFrame()
ctr = 0
# print(resp['ProductFilterResponse']['Buckets'])
# exit()
dct = {}
for data in resp['ProductFilterResponse']['Buckets']:
    # print(data)
    # exit()
    dct[data] = 0
    for data_2 in resp['ProductFilterResponse']['Buckets'][data]['Items']:

        df.at[ctr, 'Product_Category'] = 'Clothing'
        df.at[ctr, 'Category'] = 'Women'
        df.at[ctr, 'Subcategory1'] = 'Western' 
        df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
        df.at[ctr, 'Subcategory3'] = 'Dresses'
        df.at[ctr, 'Attr_Name'] = data
        df.at[ctr, 'Attr_Value'] = data_2['Title']
        dct[data] += data_2['Count']
        df.at[ctr, 'Url'] = f'https://dyn.dessy.com/api/fastnav/parseUrl/?countrycode=us&currencycode=USD&addbuckets=displaydessyus&url=%2F{data_2["Link"]}%2F%3Fpage%3D0%26rpp%3D36'
        ctr += 1
    print(len(df))
print(dct)
df.to_csv('Dessy_links.csv')