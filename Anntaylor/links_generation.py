import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

resp = BeautifulSoup(requests.get('https://www.anntaylor.com/on/demandware.store/Sites-AnnTaylor-Site/default/Search-ShowAjax?cgid=cata000016&page=0',
                                  headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}).text,'html.parser')

# print(resp)
# print(resp.find('div', {'class': 'filter-refinement-bar'}).text)

# exit()
df, ctr = pd.DataFrame(), 0
# for i, data in enumerate(resp.find_all('li', {'class': 'refinement'})):
#     # for data_2 in resp['refinementsMap']['color']['values']:
#     # print(data)
for data_2 in resp.find('div', {'class': 'filter-refinement-bar'}).find_all('div', {'class': 'refinement-body'}):
    # print(data_2)
    for data_3 in data_2.find_all('li'):
        try:
            df.at[ctr, 'Category'] = 'Women'
            df.at[ctr, 'Product_Category'] = 'Clothing'
            df.at[ctr, 'Subcategory1'] = 'Western'
            df.at[ctr, 'Subcategory2'] = 'Bottomwear'
            df.at[ctr, 'Subcategory3'] = 'Skirts'
            df.at[ctr, 'Url'] = f'https://www.anntaylor.com/on/demandware.store/Sites-AnnTaylor-Site/default/Search-ShowAjax{data_3.find("a")["href"]}&start=0&sz=16&pageTypeContext=Search-Show'
            # https://www.aliceandolivia.com/on/demandware.store/Sites-aando-Site/default/Search-UpdateGrid?cgid=dresses&start=24&sz=24&selectedUrl=https%3A%2F%2Fwww.aliceandolivia.com%2Fon%2Fdemandware.store%2FSites-aando-Site%2Fdefault%2FSearch-UpdateGrid%3Fcgid%3Ddresses%26start%3D24%26sz%3D24
            df.at[ctr, 'Attr_Name'] = data_2.find('span', {'class': 'selected-assistive-text'}).text.split(':')[0].replace('Refine by' , '').strip()
            df.at[ctr, 'Attr_Value'] = data_3.find('label')['data-attribute']
            ctr += 1
        except:
            pass

df.to_csv('anntaylor_skirts_links.csv', index=False, index_label=False) 