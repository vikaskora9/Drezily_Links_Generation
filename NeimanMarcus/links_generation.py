import requests
import json
import pandas as pd
url = 'https://www.neimanmarcus.com/c/dt/api/productlisting?categoryId=cat43810733&page=1&parentCategoryId=cat58290731&siloCategoryId=cat000001&navPath=cat000000_cat000001_cat58290731_cat43810733'
resp = json.loads(requests.get(url).text)
upd_url = 'https://www.neimanmarcus.com/c/womens-clothing-clothing-dresses-cat43810733?navpath=cat000000_cat000001_cat58290731_cat43810733&page=-0'
df, ctr = pd.DataFrame(), 0
for attr in resp['applicableFilters']:
    if attr['filterKey'] in ['Designer', 'Sale', 'Availability', 'Bucket 2', 'Size']: continue
    for attr_value in attr['facets']:
        print(attr['filterKey'], attr_value)
        df.at[ctr, 'Category'] = 'Women'
        df.at[ctr, 'Product_Category'] = 'Clothing'
        df.at[ctr, 'Subcategory1'] = 'Western'
        df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
        df.at[ctr, 'Subcategory3'] = 'Dresses'
        df.at[ctr, 'Url'] = f"{upd_url}&{attr['filterKey']}={attr_value}"
        df.at[ctr, 'Attr_Name'] = attr['filterKey']
        
        df.at[ctr, 'Attr_Value'] = attr_value
        ctr += 1

df.to_csv('neiman_marcus_dreeses_filters.csv', index=False, index_label=False)