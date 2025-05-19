import traceback

import requests
import pandas as pd
from  bs4 import BeautifulSoup


resp = BeautifulSoup(requests.get('https://www.marksandspencer.com/us/l/women/dresses-and-jumpsuits/?fhAbTestParam=&isAjax=true&fhParams=fh_view_size%3D36%26fh_merch_group%3Dnorth_america%26fh_view%3Dlister%26fh_refpath%3D3d25caad-e9f5-4828-a3ef-413b4ab100cd%26fh_country%3Dus%26fh_refview%3Dlister%26fh_reffacet%3Dproductdefinition%26fh_location%3D%2F%2Froot%2Fen_US%2Fcategories%253C%257Broot_euzzzzsczzzzlevelzzzz1zzzz1000001%257D%2Fcategories%253C%257Broot_euzzzzsczzzzlevelzzzz1zzzz1000001_euzzzzsubcategoryzzzz1002041%257D%2Fproductdefinition%253E%257Bdresses%257D&catCount=2.0&cgid=EU_SubCategory_1002041').text, 'html.parser')
final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value'])
ctr = 0
valid_attr = ['productstyle', 'fit', 'refinementcolor', 'productmaterial', 'sleevelength', 'productlength', 'fabrictype']
for data in resp.find_all('ul'):
    for ftr in data.find_all('li'):
        try:
            if ftr.find('input')['data-filterkey'] in valid_attr:
                final_df.at[ctr, 'Product_Category'] = 'Clothing'
                final_df.at[ctr, 'Category'] = 'Women'
                final_df.at[ctr, 'Subcategory1'] = 'Western'
                final_df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
                final_df.at[ctr, 'Subcategory3'] = 'Dresses'
                final_df.at[
                    ctr, 'Url'] = f"https://www.marksandspencer.com/us/l/women/dresses-and-jumpsuits/?fhAbTestParam=&isAjax=true&fhParams={ftr.find('input')['data-href']}"
                final_df.at[ctr, 'Attr_Name'] = ftr.find('input')['data-filterkey']

                final_df.at[ctr, 'Attr_Value'] = ftr.find('span', {'class': 'facet-value'}).text.strip()
                final_df.at[ctr, 'Counts'] = ftr.find('span', {'class': 'product-count'}).text.strip()
                ctr += 1
        except Exception as e:
            print(e, traceback.format_exc())
            continue

final_df.to_csv('Marksandspencer.csv', index_label=False, index=False)