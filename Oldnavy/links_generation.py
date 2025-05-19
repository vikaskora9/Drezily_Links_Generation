from copy import deepcopy

import pandas as pd
import requests
import json
# initial link:- https://api.gap.com/commerce/search/products/v2/cc?brand=on&market=us&cid=15292&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&vendor=Certona&trackingid=59358774024779
# after filter:- https://api.gap.com/commerce/search/products/v2/cc?brand=on&market=us&cid=15292&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&sleeveLength=1927%2C1928%2C1929&vendor=Certona&trackingid=59358774024779
df = pd.read_csv('/Users/shardakora/Desktop/Drezily_Scrapypoet/scrapyPageObjects/spiders/pages/Oldnavy/Women/links.csv')
final_df = pd.DataFrame(columns=[*df.columns.tolist(), 'Attr_Name', 'Attr_Value'])
for i, row in df.iterrows():
    attr_lst = json.loads(requests.get(row['Url'],
                                       headers={
                                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
                                           'path': row['Url'].replace('https://api.gap.com/', ''),
                                           'scheme': 'https',
                                           'Accept': '*/*',
                                           'Accept-Encoding': 'gzip, deflate, br',
                                           'Accept-Language': 'en-US,en;q=0.9',
                                           'Origin': 'https://oldnavy.gap.com',
                                           'Referer': 'https://oldnavy.gap.com/',
                                           'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"'
                                       }
                                       ).text)
    print(attr_lst['facets'], row['Url'])
    # attr_value -> tank tops + sc3 -> t-shirts -> sc3 = Tops
    for attr in attr_lst['facets']:
        try:
            for attr_value in attr['options']:
                tmp_df = deepcopy(row)
                tmp_df['Attr_Name'] = attr['localeName']
                tmp_df['Attr_Value'] = attr_value['localeName']
                tmp_df['Url'] = tmp_df['Url'].replace('includeMarketingFlagsDetails=true',
                                                      f'includeMarketingFlagsDetails=true&{attr["name"]}={attr_value["name"]}')
                final_df = final_df._append(tmp_df)
                # final_df = pd.concat([final_df, pd.DataFrame(tmp_df)])

        except Exception as e:
            print(attr['localeName'], e)
        print(len(final_df))
final_df.to_csv('oldnavy_bottomwear_links_with_attrs.csv', index=False, index_label=False)
