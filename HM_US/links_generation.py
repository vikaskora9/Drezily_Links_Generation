from copy import deepcopy

import pandas as pd
import requests
import json

from bs4 import BeautifulSoup
# https://api.hm.com/search-services/v1/en_us/listing/resultpage?pageSource=PLP&page=-0&sort=RELEVANCE&pageId=/ladies/shop-by-product/cardigans-and-jumpers&page-size=36&categoryId=ladies_cardigansjumpers&facets=colorWithNames:beige_f5f5dc&filters=sale:false%7C%7ColdSale:false&touchPoint=DESKTOP&skipStockCheck=false
# url = 'https://api.hm.com/search-services/v1/en_us/listing/resultpage?pageSource=PLP&page=2&sort=RELEVANCE&pageId=/ladies/shop-by-product/cardigans-and-jumpers&page-size=36&categoryId=ladies_cardigansjumpers&facets=colorWithNames:beige_f5f5dc&filters=sale:false||oldSale:false&touchPoint=DESKTOP&skipStockCheck=false'
# resp = requests.get(url)
# print(resp.text)
# df = pd.DataFrame()
# i = 0
# for data in resp['props']['pageProps']['pageData']['content'][5]['pillsList']:
#     df.at[i, 'Product_Category'] = 'Clothing'
#     df.at[i, 'Product_Type'] = data['title']
#     df.at[i, 'Category'] = 'Women'
#     df.at[i, 'Subcategory1'] = 'Western'
#     df.at[i, 'Subcategory2'] = 'Dresses and Jumpsuits'
#     df.at[i, 'Subcategory3'] = 'Dresses'
#     df.at[i, 'Url'] = f"https://www2.hm.com{data['path']}"
#     i += 1
# df.to_csv('hm_us_links.csv', index_label=False, index=False)
# exit()
# attr_mapp = {
#     "colorWithNames": 'Native_Colour',
#     "clothingStyles": ' Style',
# "necklineStyles": 'Neckline',
# "sleeveLengths": 'Sleeve_Length',
# "garmentLengths": 'Length',
# "sleeveStyles": 'Sleeve_Styling',
# "fits": 'Fit',
#     "contexts": 'Occassion',
# "materials": 'Fabric'
# }
# df = pd.read_csv('hm_us_links.csv')
final_df = pd.DataFrame()
inde = 0
url = 'https://api.hm.com/search-services/v1/en_us/listing/resultpage?pageSource=PLP&page=2&sort=RELEVANCE&pageId=/ladies/shop-by-product/dresses&page-size=36&categoryId=ladies_dresses&filters=sale:false||oldSale:false&touchPoint=DESKTOP&skipStockCheck=false'
attr_lst = json.loads(requests.get(url).text)
    # print(attr_lst, row['Url'])
dct = {}
for attr in attr_lst['plpList']['facets']:
# https://www2.hm.com/en_us/women/products/cardigans-sweaters.html?colorWithNames=black_000000
    # print(attr['name'])
    dct[attr['name']] = 0
    try:
        for attr_value in attr['filterValues']:
            # tmp_df = deepcopy(row)
            try:
                # print(attr_value)
                tmp_df = dict()
                final_df.at[inde, 'Category'] = 'Women'
                final_df.at[inde, 'Subcategory1'] = 'Western'
                final_df.at[inde, 'Subcategory2'] = 'Outerwear'
                final_df.at[inde, 'Subcategory3'] = 'Hoodies & Sweatshirts'
                final_df.at[inde, 'Attr_Name'] = attr['name']
                final_df.at[inde, 'Attr_Value'] = attr_value['name'].split('_')[0].title().strip()
                final_df.at[inde, 'Url'] = url.replace('&filters', f"&facets={attr['id']}:{attr_value['name']}&filters")
                dct[attr['name']] += attr_value['count']
                # tmp_df['Attr_Value'] = 
                # tmp_df['Url'] = f"{tmp_df['Url']}?{attr['id']}={attr_value['id']}"
                # final_df = final_df.append(tmp_df, ignore_index=True)
                inde += 1
            except Exception as e:
                print(e)
                continue
    except Exception as e:
        print(attr['name'], e)
        pass

    print(len(final_df))
print(dct)
final_df.to_csv('hm_us_hoodies_sweatshirts.csv', index=False, index_label=False)
