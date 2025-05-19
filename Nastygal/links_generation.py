import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

resp = json.loads(requests.get('https://www.nastygal.com/on/demandware.store/Sites-nastygal-US-Site/en_US/Search-ExpandRefinement?expandedOnly=1&cgid=tops&expanded=color&ajax=true').text)

df, ctr = pd.DataFrame(), 0
for i, data in enumerate(resp['refinementsMap']):
    for data_2 in resp['refinementsMap']['color']['values']:
        # df.at[ctr, 'Category'] = 'Women'
        # df.at[ctr, 'Product_Category'] = 'Clothing'
        # df.at[ctr, 'Subcategory1'] = 'Western'
        # df.at[ctr, 'Subcategory2'] = 'Topwear'
        # df.at[ctr, 'Subcategory3'] = 'Topwear'
        # df.at[ctr, 'Url'] = f'https://www.nastygal.com{data_2["url"]}&start=0&sz=16&pageTypeContext=Search-Show'
        df.at[ctr, 'Attr_Name'] = resp['refinementsMap']['color']['displayName']
        
        df.at[ctr, 'Attr_Value'] = data_2['displayValue']
        ctr += 1

df.to_csv('nastygal_dreeses_filters.csv', index=False, index_label=False)