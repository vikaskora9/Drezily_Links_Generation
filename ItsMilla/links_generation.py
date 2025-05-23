import requests
import pandas as pd
from bs4 import BeautifulSoup

resp = BeautifulSoup(requests.get('https://itsmilla.com/collections/all-dresses?filter.v.price.gte=0&filter.v.price.lte=1600.00&filter.p.product_type=Dress&sort_by=manual').text, 'html.parser')

df, ctr = pd.DataFrame(), 0
for filter in resp.find('div', {'class':'filter-content'}).find_all('div', {'class': 'filter-block'}):
    # print(filter.find('button')['controls'] if filter.find('button') is not None else '')
    try:
        # print(filter.find('div', {'class': 'collapsible-content'})['id'])
        attr_name = filter.find('div', {'class': 'collapsible-content'})['id'].replace('collapsible-', '')
        for attr_value in filter.find_all('div', {'class':'filter-value-item'}):
            # if 'collapsible' in attr_value.find('input')['value']:
            #     continue
            df.at[ctr, 'Product_Category'] = 'Clothing'
            df.at[ctr, 'Category'] = 'Women'
            df.at[ctr, 'Subcategory1'] = 'Western'
            df.at[ctr, 'Subcategory2'] = 'Dresses and Jumsuits'
            df.at[ctr, 'Subcategory3'] = 'Dresses'
            df.at[ctr, 'Url'] = f"https://itsmilla.com/collections/all-dresses?{attr_value.find('input')['name']}={attr_value.find('input')['value']}&sort_by=manual"
            df.at[ctr, 'Attr_Name'] = attr_name
            df.at[ctr, 'Attr_Value'] = attr_value.find('input')['value']
            print(attr_value.find('input')['value'])
            ctr += 1
    except Exception as e:
        print(e)
        pass
    # break

df.to_csv('itsmilla_dresses_links.csv', index=False, index_label=False)