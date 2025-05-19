import pandas as pd
import json
import requests

tmp_df = pd.DataFrame()
ind = 0
# https://api.gap.com/commerce/search/products/v2/cc?brand=br&market=us&cid=69883&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&enableSwatchSort=true&sortSwatchesBy=newness&occasion=178282644&vendor=Certona&trackingid=309892845958361
# https://api.gap.com/commerce/search/products/v2/cc?brand=br&market=us&cid=69883&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&enableSwatchSort=true&sortSwatchesBy=newness&vendor=Certona&trackingid=309892845958361
attr_lst = json.loads(requests.get('https://api.gap.com/commerce/search/products/v2/cc?brand=br&market=us&cid=69883&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&enableSwatchSort=true&sortSwatchesBy=newness&department=136&vendor=constructorio&client_id=f7cbad04-c8be-456b-824f-871ab3a6e41a&session_id=13',
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
                        'path': '/commerce/search/products/v2/cc?brand=br&market=us&cid=99915&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&enableSwatchSort=true&sortSwatchesBy=newness&occasion=178282644&vendor=Certona&trackingid=309892845958361',
                        'scheme': 'https',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Origin': 'https://bananarepublic.gap.com',
                        'Referer': 'https://bananarepublic.gap.com/',
                        'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"'
                    }
                    ).text)
for attr in attr_lst['facets']:
    try:
        for attr_value in attr['options']:
            # tmp_df.at[ind, 'Product_Category'] = 'Clothing'
            # tmp_df.at[ind, 'Category'] = 'Women'
            # tmp_df.at[ind, 'Subcategory1'] = 'Western'
            # tmp_df.at[ind, 'Subcategory2'] = 'Topwear'
            # tmp_df.at[ind, 'Subcategory3'] = 'Tops & Blouses'
            tmp_df.at[ind, 'Attr_Name'] = attr['localeName']
            tmp_df.at[ind, 'Attr_Value'] = attr_value['localeName']
            print(attr_value['name'])
            # exit()
            # tmp_df.at[ind, 'Url'] = 'https://api.gap.com/commerce/search/products/v2/cc?brand=br&market=us&cid=5037&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&enableSwatchSort=true&sortSwatchesBy=newness&vendor=Certona&trackingid=309892845958361'.replace('sortSwatchesBy=newness', f'sortSwatchesBy=newness&{attr["name"]}={attr_value["name"]}')
            # final_df = final_df.append(tmp_df)
            ind += 1
    except:
        print(attr['localeName'])
tmp_df.to_csv('banana_republic_dresses_filter.csv', index_label=False, index=False)