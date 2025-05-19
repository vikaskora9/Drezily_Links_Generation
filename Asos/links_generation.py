from copy import deepcopy
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

# resp = requests.get('https://www.asos.com/api/product/search/v2/categories/9263?offset=0&includeNonPurchasableTypes=restocking&store=US&lang=en-US&currency=USD&rowlength=3&channel=desktop-web&country=US&customerLoyaltyTier=0&keyStoreDataversion=mhabj1f-41&advertisementsPartnerId=100716&advertisementsVisitorId=4f89d8e4-c48b-4269-b118-4ff58b2ec3d9&advertisementsOptInConsent=true&limit=72')
# resp = requests.get('https://www.asos.com/us/mamalicious/mamalicious-maternity-ribbed-top-and-flared-pants-set-in-cream/grp/208229254#colourWayId-207585338&productId-207585328',
#                     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'})
# pdp_data = BeautifulSoup(resp.text, 'html.parser')
# Image_Urls = [img.find('img')['src'].replace('240w', '1920w').replace('40&', '1926&') for img in pdp_data.find_all('li', {'class': 'image-thumbnail'})]
# print(Image_Urls)
# exit()
# df = pd.read_csv('C:/Users/vikas/PycharmProjects/Drezily_Scrapypoet/scrapyPageObjects/spiders/pages/Asos/Women/links.csv')
final_df = pd.DataFrame()
index = 0
# valid_attr_lst = ['Style', 'Neckline', 'Sleeve Length', 'Body Fit', 'Length', 'Color', 'Product Type']
# for i, row in df.iterrows():
url = 'https://www.asos.com/api/product/search/v2/categories/8799?offset=0&includeNonPurchasableTypes=restocking&store=US&lang=en-US&currency=USD&rowlength=4&channel=desktop-web&country=US&customerLoyaltyTier=null&keyStoreDataversion=4i7nlxk-44&advertisementsPartnerId=100716&advertisementsVisitorId=4f89d8e4-c48b-4269-b118-4ff58b2ec3d9&advertisementsOptInConsent=true&limit=72'
# url = 'https://www.asos.com/api/product/search/v2/categories/15200?offset=0&includeNonPurchasableTypes=restocking&store=US&lang=en-US&currency=USD&rowlength=4&channel=desktop-web&country=US&customerLoyaltyTier=null&keyStoreDataversion=4i7nlxk-44&advertisementsPartnerId=100716&advertisementsVisitorId=4f89d8e4-c48b-4269-b118-4ff58b2ec3d9&advertisementsOptInConsent=true&limit=72'
attr_lst = json.loads(requests.get(url).text)['facets']
dct = {}
for attr in attr_lst:
    if attr['name'] not in ['Price Range', 'Brand', 'Size']:
        dct[attr['name']] = 0 
        for attr_value in attr['facetValues']:
            final_df.at[index, 'Product_Category'] = 'Clothing'
            final_df.at[index, 'Category'] = 'Women'
            final_df.at[index, 'Subcategory1'] = 'Western'
            final_df.at[index, 'Category2'] = 'Dresses and Jumpsuits'
            final_df.at[index, 'Category3'] = 'Dresses'
            dct[attr['name']] += attr_value['count']
            final_df.at[index, 'Url'] = url.replace('&limit=72', f'&limit=72&{attr["id"]}={attr_value["id"]}')
            final_df.at[index, 'Attr_Name'] = attr['name']
            final_df.at[index, 'Attr_Value'] = attr_value['name']
            # tmp_df['Url'] = tmp_df['Url']
            # final_df = final_df.append(tmp_df)
            index += 1
        print(len(final_df))
print(dct)
final_df.to_csv('Dresses_Length_asos_filters.csv', index=False, index_label=False)