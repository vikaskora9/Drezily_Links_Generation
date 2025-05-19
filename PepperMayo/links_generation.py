import requests
import json
import pandas as pd

#                               https://5crv30.a.searchspring.io/api/search/search.json?userId=77cb8fe7-64a9-478a-9740-bdcbfcf0a632&domain=https%3A%2F%2Fpeppermayo.com%2Fcollections%2Fdresses
# %23%2Ffilter%3Atags_type%3AMaxi%242520Dresses&
#                                                                                                                                                                                               sessionId=1b5d6fc5-5d56-4582-a2e5-e91464fde3fa&pageLoadId=87a9ca92-70a6-43df-90c0-0f4ad4872a39&siteId=5crv30&
# filter.tags_type=Maxi%20Dresses&
#
# bgfilter.collection_handle=dresses&redirectResponse=full&ajaxCatalog=Snap&resultsFormat=native
upd_url = 'https://5crv30.a.searchspring.io/api/search/search.json?userId=77cb8fe7-64a9-478a-9740-bdcbfcf0a632&domain=https%3A%2F%2Fpeppermayo.com%2Fcollections%2Fdresses&sessionId=1b5d6fc5-5d56-4582-a2e5-e91464fde3fa&pageLoadId=87a9ca92-70a6-43df-90c0-0f4ad4872a39&siteId=5crv30&bgfilter.collection_handle=dresses&redirectResponse=full&ajaxCatalog=Snap&resultsFormat=native'
resp = json.loads(requests.get('https://5crv30.a.searchspring.io/api/search/search.json?userId=77cb8fe7-64a9-478a-9740-bdcbfcf0a632&domain=https%3A%2F%2Fpeppermayo.com%2Fcollections%2Fdresses&sessionId=1b5d6fc5-5d56-4582-a2e5-e91464fde3fa&pageLoadId=87a9ca92-70a6-43df-90c0-0f4ad4872a39&siteId=5crv30&bgfilter.collection_handle=dresses&redirectResponse=full&ajaxCatalog=Snap&resultsFormat=native').text)


df, ctr = pd.DataFrame(), 0
for attr in resp['facets']:
    for attr_value in attr['values']:
        print(attr['label'], attr_value)
        df.at[ctr, 'Category'] = 'Women'
        df.at[ctr, 'Product_Category'] = 'Clothing'
        df.at[ctr, 'Subcategory1'] = 'Western'
        df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
        df.at[ctr, 'Subcategory3'] = 'Dresses'
        df.at[ctr, 'Url'] = upd_url.replace('siteId=5crv30&', f"siteId=5crv30&%23%2Ffilter%3A{attr['field']}%3A{attr_value['value']}&").replace('bgfilter.collection_handle', f'filter.{attr["field"]}={attr_value["value"]}&bgfilter.collection_handle')
        df.at[ctr, 'Attr_Name'] = attr['label']
        
        df.at[ctr, 'Attr_Value'] = attr_value['value']
        ctr += 1

df.to_csv('pinkblush_dreeses_filters.csv', index=False, index_label=False)