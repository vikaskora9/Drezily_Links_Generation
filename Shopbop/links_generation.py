from copy import deepcopy

import pandas as pd
import requests
import json
# initial link:- https://api.shopbop.com/public/products?siteId=1000&lang=en-IN&currency=USD&categoryId=13351&facetAllowList=T2&offset=0&limit=100&includeFacets=true&disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT
# after filter:- https://api.shopbop.com/public/products?siteId=1000&lang=en-IN&currency=USD&categoryId=13351&facetAllowList=T2&offset=0&limit=100&includeFacets=true&f=MADressStyle-A-Line&disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT
# df = pd.re÷ad_csv('C:/Users/vikas/PycharmProjects/Drezily_Scrapypoet/scrapyPageObjects/spiders/pages/Shopbop/Women/links.csv')
# final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value'])

attr_lst = json.loads(requests.get('https://api.shopbop.com/public/products?siteId=1000&lang=en-IN&currency=USD&categoryId=13377&facetAllowList=C&offset=100&limit=100&includeFacets=true&disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT'
                                   # headers={
                                   #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
                                   #     'path': '/commerce/search/products/v2/cc?brand=on&market=us&cid=15292&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&pageNumber=1&vendor=Certona&trackingid=806429477362237',
                                   #     'scheme': 'https',
                                   #     'Accept': '*/*',
                                   #     'Accept-Encoding': 'gzip, deflate, br',
                                   #     'Accept-Language': 'en-US,en;q=0.9',
                                   #     'Origin': 'https://oldnavy.gap.com',
                                   #     'Referer': 'https://oldnavy.gap.com/',
                                   #     'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"'
                                   # }
                                   ).text)
# print(attr_lst, row['Url'])
tmp_df = pd.DataFrame()
inde = 0
for attr in attr_lst['sortAndFilterOptions']['facets']:
    try:
        for attr_value in attr['fieldSets']:
            for attr_value_2 in attr_value['filters']:
                tmp_df.at[inde, 'Product_Category']= 'Clothing'
                tmp_df.at[inde, 'Category']= 'Women'
                tmp_df.at[inde, 'Subcategory1']= 'Western'
                tmp_df.at[inde, 'Subcategory2']= 'Bottomwear'
                tmp_df.at[inde, 'Subcategory3']= 'Jeans'
                tmp_df.at[inde, 'Attr_Name'] = attr_value['legend']
                tmp_df.at[inde, 'Attr_Value'] = attr_value_2['label']
                # tmp_df['Url'] = f'https://api.shopbop.com/public/products?siteId=1000&lang=en-IN&currency=USD&categoryId=13351&facetAllowList=T2&offset=0&limit=100&includeFacets=true&f={attr_value_2["id"]}&disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT'
                # tmp_df['Url'] = f'https://api.shopbop.com/public/products?siteId=1000&lang=en-US&currency=USD&categoryId=13332&facetAllowList=C&offset=0&limit=100&includeFacets=true&f={attr_value_2["id"]}&disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT'
                # tmp_df.at[inde, 'Url'] = f'https://api.shopbop.com/public/products?siteId=1000&lang=en-US&currency=USD&categoryId=13414&facetAllowList=C&offset=-0&limit=100&includeFacets=true&f={attr_value_2["id"]}&disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT'
                # tmp_df.at[inde, 'Url'] = f'https://api.shopbop.com/public/products?siteId=1000&lang=en-US&currency=USD&categoryId=13317&facetAllowList=C&offset=-0&limit=100&includeFacets=true&f={attr_value_2["id"]}disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT'
                tmp_df.at[inde, 'Url'] = f'https://api.shopbop.com/public/products?siteId=1000&lang=en-IN&currency=USD&categoryId=13377&facetAllowList=C&offset=100&limit=100&includeFacets=true&f={attr_value_2["id"]}disableSiteEligibilityFiltering=true&imageStrategy=Q_ASPECT'
                # final_df = final_df.concat(tmp_df, ignore_index=True)
                inde += 1
    except Exception as e:
        print(attr_value['legend'], e)
    print(len(tmp_df))
tmp_df.to_csv('shopbop_jeans_links_with_attrs.csv', index=False, index_label=False)
