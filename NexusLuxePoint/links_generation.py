import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

resp = BeautifulSoup(requests.get('https://nexuspointluxe.com/collections/dresses?geo_hide_market=1').text, 'html.parser')
# print(len(resp))
# exit()
df = pd.DataFrame()
ctr = 0
att_val = [color['data-tooltip'].replace(' ', '+').strip() for color in resp.find('div', {'class': 'color-swatch-list'}).find_all('div', {'class': 'color-swatch'})]
for attr in att_val:
    df.at[ctr, 'Product_Category'] = 'Clothing'
    df.at[ctr, 'Category'] = 'Women'
    df.at[ctr, 'Subcategory1'] = 'Western'
    df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
    df.at[ctr, 'Subcategory3'] = 'Dresses'
    df.at[ctr, 'Url'] = f"https://nexuspointluxe.com/collections/dresses?filter.v.option.color={attr}"
    df.at[ctr, 'Attr_Name'] = 'Color'
    df.at[ctr, 'Attr_Value'] = attr.replace('++', '+').replace('+', ' ').title()
    ctr+=1
df.to_csv('NexusLuxePoint_Dresses.csv', index_label=False, index=False)
exit()
# resp_json = json.loads(resp.text)

final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value'])
valid_attr_lst = ['Color', 'Pattern', '7::Fabric', '2::Length', '6::Silhouette', '1::Occasion']
ctr = 0
attr_lst = json.loads(resp.text)['refinements']
for attr in attr_lst:
    if attr['label'] in valid_attr_lst:
        print(attr['label'], attr['attribute_id'])
        # continue

        for attr_value in attr['values']:
            final_df.at[ctr, 'Product_Category'] = 'Clothing'
            final_df.at[ctr, 'Category'] = 'Women'
            final_df.at[ctr, 'Subcategory1'] = 'Western'
            final_df.at[ctr, 'Subcategory2'] = 'Topwear'
            final_df.at[ctr, 'Subcategory3'] = 'Tops'
            final_df.at[ctr, 'Url'] = f'https://www.jcrew.com/browse/product_search?expand=variations%2Cavailability&count=60&start=0&refine=c_allowedCountries%3DALL%7CUS&refine_1=c_displayOn%3Dstandard_usd&' \
                                      f'refine_2={attr["attribute_id"]}%3D{attr_value["label"]}&refine_3=cgid%3Dwomens%7Ccategories%7Cclothing%7Cdresses-and-jumpsuits&refine_4=isAppExclusive%3Dfalse&country-code=US' \
                                      f'&seo-word-cloud-key=%2Fwomens%2Fcategories%2Fclothing%2Fdresses-and-jumpsuits%2F{attr["label"].lower()}%3D{attr_value["label"]}'
            final_df.at[ctr, 'Attr_Name'] = attr['label']
            try:
                final_df.at[ctr, 'Attr_Value'] = attr_value['description']
            except:
                final_df.at[ctr, 'Attr_Value'] = attr_value['value']
            final_df.at[ctr, 'Counts'] = attr_value['hit_count']
            ctr += 1
print(len(final_df))
final_df.to_csv('JCrew_links_with_attrs.csv', index=False, index_label=False)