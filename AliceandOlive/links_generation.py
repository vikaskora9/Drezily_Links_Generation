import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

resp = BeautifulSoup(requests.get('https://www.aliceandolivia.com/on/demandware.store/Sites-aando-Site/default/Search-ShowAjax?cgid=dresses&start=24&sz=24').text,'html.parser')

# print(resp)
# print(resp.find('span', {'class': 'bfx-list-price'}))

# exit()
df, ctr = pd.DataFrame(), 0
# for i, data in enumerate(resp.find_all('li', {'class': 'refinement'})):
#     # for data_2 in resp['refinementsMap']['color']['values']:
#     # print(data)
for data_2 in resp.find('div', {'class': 'refinement-bar'}).find_all('li', {'class': 'filter-options-list'}):
    print(data_2)
    # df.at[ctr, 'Category'] = 'Women'
    # df.at[ctr, 'Product_Category'] = 'Clothing'
    # df.at[ctr, 'Subcategory1'] = 'Western'
    # df.at[ctr, 'Subcategory2'] = 'Bottomwear'
    # df.at[ctr, 'Subcategory3'] = 'Shorts'
    # df.at[ctr, 'Url'] = f'https://www.aliceandolivia.com{data_2.find("button")["data-href"]}&start=0&sz=16&pageTypeContext=Search-Show'
    # https://www.aliceandolivia.com/on/demandware.store/Sites-aando-Site/default/Search-UpdateGrid?cgid=dresses&start=24&sz=24&selectedUrl=https%3A%2F%2Fwww.aliceandolivia.com%2Fon%2Fdemandware.store%2FSites-aando-Site%2Fdefault%2FSearch-UpdateGrid%3Fcgid%3Ddresses%26start%3D24%26sz%3D24
    df.at[ctr, 'Attr_Name'] = data_2.find('input')['name']
    df.at[ctr, 'Attr_Value'] = data_2.find('span')['data-refinement-value']
    ctr += 1

df.to_csv('aliceandolive_dresses_filer.csv', index=False, index_label=False) 