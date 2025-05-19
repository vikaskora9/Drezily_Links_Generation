from copy import deepcopy
import math

import pandas as pd
import requests
import json
# {'TOP': 11898, 'JEANS': 6610, 'JACKET': 2644, 'HANDBAG': 9254, 'BRA': 2644, 'LINGERIE': 661, 'SHOE': 25118, 'DRESS': 5949, 'SWEATER': 6610, 'COAT': 1983, 'PANTY': 1322, 'PANTS': 4627, 'SLEEPWEAR': 1322, 'BATH_ROBE': 1983, 'SCARF': 661, 'SWEATSHIRT': 661, 'SOCK': 661}
from bs4 import BeautifulSoup
url = 'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/dresses&id=5449&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_additionalStoreLocations=5076&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0195b80f4d320004778f7d8a0cda0507701e306f00992&visitorId=60281118009897967283305714561101324458&customerId=&_deviceType=DESKTOP&_customerState=GUEST&_customerExperiment=1162-21,2051-21,2054-24,2111-11,2116-21,2132-21,2135-21,2137-21,2150-21,2151-21,2160-21,2161-11,2451-21,2465-20,2486-20,2490-20'
api_res = json.loads(requests.get(url,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}).text)
# resp = requests.get('https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-tops&id=255&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_additionalStoreLocations=5133&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=01924d4e5a27001a8f34c6bd74680507d01d3075007e8&visitorId=80934390978429631027343511310562026974&customerId=&_deviceType=DESKTOP&_customerState=GUEST&_customerExperiment=1086-21,1162-21,1167-21,2015-21,2026-21,2027-11,2051-21,2054-21,2063-21,2111-11,835-21',
#                     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'})
# dist_subcate3 = dict()
# pgs = resp['body']['canvas']['rows'][0]['rowSortableGrid']['zones'][1]['sortableGrid']['model'][
#                 'pagination'][
#                 'numberOfPages']
# print(pgs)
# pg_url = []
# for pg in range(1, math.ceil(pgs / 2) + 1):
#             pg_url.append(url.replace('productsPerPage=60', 'productsPerPage=120').replace('pageIndex=1',
#                                                                                                          f'pageIndex={pg}'))
# for url in pg_url:
#     resp = requests.get(url,
#                                 headers={
#                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'})
#     gallery_data = json.loads(resp.text)
    
#     for _, prods in enumerate(
#                 gallery_data['body']['canvas']['rows'][0]['rowSortableGrid']['zones'][1]['sortableGrid']['collection']):
#             try:
#                 if prods['product']['detail']['typeName'] in dist_subcate3:
#                     dist_subcate3[prods['product']['detail']['typeName']] += 1
#                 else:
#                     dist_subcate3[prods['product']['detail']['typeName']] = 1
#             except Exception as e:
#                   print(e)
#                   pass
# print(dist_subcate3)
# # print(api_res)
# exit()
final_df = pd.DataFrame(columns=['Attr_Name', 'Attr_Value'])
ctr = 0
# valid_attr_list = ['Occasion', 'Color', 'Dress Style', 'Dress Length', 'Sleeve Length', 'Pattern', 'Neckline', 'Fabric']
ct_dct = {}
for attr in api_res['body']['canvas']['rows'][0]['rowSortableGrid']['zones'][0]['facets']['facets']:
    # if attr['displayName'] in valid_attr_list:
        print(attr['displayName'])
        try:
            if attr['displayName'] in ['Size', 'Price', 'Designer', 'Sales & Offers', 'Percent Off']:
                 continue
            ct_dct[attr['displayName']] = 0
            for attr_value in attr['values']:
                final_df.at[ctr, 'Product_Category'] = 'Clothing'
                final_df.at[ctr, 'Category'] = 'Women'
                final_df.at[ctr, 'Subcategory1'] = 'Western'
                final_df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
                final_df.at[ctr, 'Subcategory3'] = 'Dresses'
                final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/dresses{attr_value["url"]}&id=5449&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0192463b78f8001cd55be88a63310507d0016075007e8&visitorId=91466343618216206869221075540066848073&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-tops{attr_value["url"]}&id=255&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_additionalStoreLocations=5133&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=01924d4e5a27001a8f34c6bd74680507d01d3075007e8&visitorId=80934390978429631027343511310562026974&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-blazers{attr_value["url"]}&id=55429&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-blazers{attr_value["url"]}&id=55429&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-coats{attr_value["url"]}&id=269&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-sweater{attr_value["url"]}s&id=260&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/hoodies-sweatshirts{attr_value["url"]}&id=293359&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&customerId=&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.bloomingdales.com/xapi/discover/v1/page?pathname=/shop/womens-apparel/tops-tees{attr_value["url"]}&id=5619&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=2&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0195b3922e80006aab023fd734f005077008706f00992&visitorId=30630161747800883749173251732805630882&customerId=53a08e50-d5df-4c89-9522-67f63411c88d&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.bloomingdales.com/xapi/discover/v1/page?pathname=/shop/womens-apparel/designer-dresses{attr_value["url"]}&id=21683&_navigationType=BROWSE&_shoppingMode=SITE&sortBy=ORIGINAL&productsPerPage=60&pageIndex=1&_application=SITE&_regionCode=US&currencyCode=USD&size=medium&spItemsVersion=1.1&utagId=0195b3922e80006aab023fd734f005077008706f00992&visitorId=30630161747800883749173251732805630882&customerId=53a08e50-d5df-4c89-9522-67f63411c88d&_deviceType=DESKTOP&_customerState=GUEST'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-pants{attr_value["url"]}&id=157&xapi=1&_navigationType=BROWSE&_regionCode=US&currencyCode=USD&facetsOnly=true&_shoppingMode=SITE&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&_deviceType=DESKTOP&pageIndex=1&productsPerPage=60&sortBy=ORIGINAL'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-jeans{attr_value["url"]}&id=3111&xapi=1&_navigationType=BROWSE&_regionCode=US&currencyCode=USD&facetsOnly=true&_shoppingMode=SITE&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&_deviceType=DESKTOP&pageIndex=1&productsPerPage=60&sortBy=ORIGINAL'
                # final_df.at[ctr, 'Url'] = f'https://www.macys.com/xapi/discover/v1/page?pathname=/shop/womens-clothing/all-womens-clothing/womens-shorts{attr_value["url"]}&id=5344&xapi=1&_navigationType=BROWSE&_regionCode=US&currencyCode=USD&facetsOnly=true&_shoppingMode=SITE&spItemsVersion=1.1&utagId=0194836e38ce0002d6d827630db105075019e06d00992&visitorId=&_deviceType=DESKTOP&pageIndex=1&productsPerPage=60&sortBy=ORIGINAL'
                final_df.at[ctr, 'Attr_Name'] = attr['displayName']

                final_df.at[ctr, 'Attr_Value'] = attr_value['displayName']
                ct_dct[attr['displayName']] += attr_value['count']
                ctr += 1
        except:
            pass
print(ct_dct)
final_df.to_csv('Macys_dresses_filters_links.csv', index=False, index_label=False)