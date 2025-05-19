import requests
import pandas as pd
import json



api_res = json.loads(requests.get(
    'https://www.theoutnet.com/api/yoox/ton/search/resources/store/theoutnet_us/productview/byCategory?attrs=true&category=%2Fclothing%2Ftops&locale=en_US&pageNumber=2&pageSize=96',
    headers={
        # 'application-name': 'Blue lobster',
        # 'application-version': '4.774.0',
        # 'label': 'getCategoryBySeoPath',
        # # referer: https://www.theoutnet.com/en-us/shop/clothing/dresses?pageNumber=2
        # 'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': "Windows",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'x-ibm-client-id': '19c36e19-5bc7-4de4-a4a9-65ffb9dcb727'
    }).text)

# print(api_res)

# exit()
# valid_facet = ['Color', 'Fabric', 'Occasion']
final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value', 'Counts'])
ctr = 0
for facet in api_res['facets']:
    if facet['label'] not in ['Clothing Size', 'Designer', 'Size']:
        print(facet['label'])
        for facets_2 in facet['entry']:
            try:
                final_df.at[ctr, 'Product_Category'] = 'Clothing'
                final_df.at[ctr, 'Category'] = 'Women'
                final_df.at[ctr, 'Subcategory1'] = 'Western'
                final_df.at[ctr, 'Subcategory2'] = 'Topwear'
                final_df.at[ctr, 'Subcategory3'] = 'Tops'
                # https://www.theoutnet.com/api/yoox/ton/search/resources/store/theoutnet_us/productview/byCategory?attrs=true&category=%2Fclothing%2Fjeans&locale=en_US&pageNumber=1&pageSize=96
                final_df.at[
                    ctr, 'Url'] = f'https://www.theoutnet.com/api/yoox/ton/search/resources/store/theoutnet_us/productview/byCategory?attrs=true&category=%2Fclothing%2Ftops&facet={facets_2["value"]}&locale=en_US&pageNumber=2&pageSize=96'
                # try:
                final_df.at[ctr, 'Attr_Name'] = facet['label']
                final_df.at[ctr, 'Attr_Value'] = facets_2['label']
                final_df.at[ctr, 'Counts'] = facets_2['count']
                ctr+=1
                # except Exception as e:
                #     pass
            except Exception as e:
                 print(e, facets_2)



for ctr_2, facet in enumerate (api_res['facets'][0]['entry'][0]['children'][14]['children']):
    final_df.at[ctr, 'Product_Category'] = 'Clothing'
    final_df.at[ctr, 'Category'] = 'Women'
    final_df.at[ctr, 'Subcategory1'] = 'Western'
    final_df.at[ctr, 'Subcategory2'] = 'Topwear'
    final_df.at[ctr, 'Subcategory3'] = 'Tops'
    final_df.at[
        ctr, 'Url'] = f'https://www.theoutnet.com/api/yoox/ton/search/resources/store/theoutnet_us/productview/byCategory?attrs=true&category={facet["seo"]["seoURLKeyword"]}&locale=en_US&pageNumber=2&pageSize=96'
    final_df.at[ctr, 'Attr_Name'] = f'Value_{ctr_2+1}'
    final_df.at[ctr, 'Attr_Value'] = facet['label']
    final_df.at[ctr, 'Counts'] = facet['count']
    ctr += 1


final_df.to_csv('Theoutnet_Tops_2.csv', index_label=False, index=False)

