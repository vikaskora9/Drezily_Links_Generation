import requests
import json
import pandas as pd
# url = 'https://www.neimanmarcus.com/c/dt/api/productlisting?categoryId=cat43810733&page=1&parentCategoryId=cat58290731&siloCategoryId=cat000001&navPath=cat000000_cat000001_cat58290731_cat43810733'
upd_url = 'https://www.bergdorfgoodman.com/dt/api/productlisting/v2?abTestPCSVendor=EVG&categoryId=cat364409&page=1&parentCategoryId=cat441206&profileId=&siloCategoryId=cat000002'
resp = json.loads(requests.get(upd_url).text)
df, ctr = pd.DataFrame(), 0
for attr in resp['applicableFilters']:
    if attr['filterKey'] in ['Designer', 'Sale', 'Availability', 'Bucket 2', 'Size']: continue
    for attr_value in attr['facets']:
        print(attr['filterKey'], attr_value)
        df.at[ctr, 'Category'] = 'Women'
        df.at[ctr, 'Product_Category'] = 'Clothing'
        df.at[ctr, 'Subcategory1'] = 'Western'
        df.at[ctr, 'Subcategory2'] = 'Topwear'
        df.at[ctr, 'Subcategory3'] = 'Tops'
        df.at[ctr, 'Url'] = upd_url.replace('page=1', f"filterOptions=%7B%22{attr['filterKey']}%22%3A%5B%22{attr_value}%22%5D%7D&page=1")
        df.at[ctr, 'Attr_Name'] = attr['filterKey']
        
        df.at[ctr, 'Attr_Value'] = attr_value
        ctr += 1

df.to_csv('bergdorf_toops_filters.csv', index=False, index_label=False)
# 