import requests
import pandas as pd
from bs4 import BeautifulSoup


resp = BeautifulSoup(requests.get('https://www.thereformation.com/dresses').text, 'html.parser')

df, ctr = pd.DataFrame(), 0
for i, data in enumerate(resp.find('div', {'class': 'refinements'}).find_all('div', {'class': 'refinement'})):
    for data_2 in data.find_all('li'):
        # df.at[ctr, 'Category'] = 'Women'
        # df.at[ctr, 'Product_Category'] = 'Clothing'
        # df.at[ctr, 'Subcategory1'] = 'Western'
        # df.at[ctr, 'Subcategory2'] = 'Topwear'
        # df.at[ctr, 'Subcategory3'] = 'Tops'
        # df.at[ctr, 'Url'] = f'https://www.thereformation.com{data_2.find("a")["href"]}&start=0&sz=16&pageTypeContext=Search-Show'
        df.at[ctr, 'Attr_Name'] = data['class'][1]
        if len(data_2.find('span').text.strip())>0:
            df.at[ctr, 'Attr_Value'] = data_2.find('span').text.strip()
        else:
            df.at[ctr, 'Attr_Value'] = data_2.find('a')['data-refinement-id'].split('-')[-1]
        ctr += 1

df.to_csv('reformation_dresses_filter.csv', index=False, index_label=False)