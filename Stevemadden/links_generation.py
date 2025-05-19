import requests
import pandas as pd
import json
from copy import deepcopy

resp = requests.get('https://api.fastsimon.com/categories_navigation?page_num=2&products_per_page=80&facets_required=1&with_product_attributes=true&request_source=v-next&src=v-next&UUID=777f83f8-820e-45d0-a08b-08c6b432b87a&uuid=777f83f8-820e-45d0-a08b-08c6b432b87a&store_id=21708465&api_type=json&narrow=%5B%5D&sort_by=relevance&category_id=193283948677')
#
# resp_json = json.loads(resp.text)

final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value'])
valid_attr_lst = ['Color', 'Style', 'Sleeve Length', 'Length']
ctr = 0
attr_lst = json.loads(resp.text)['facets']
for attr in attr_lst:
    if attr[2] in valid_attr_lst:

        for attr_value in attr[1]:
            final_df.at[ctr, 'Product_Category'] = 'Clothing'
            final_df.at[ctr, 'Category'] = 'Women'
            final_df.at[ctr, 'Subcategory1'] = 'Western'
            final_df.at[ctr, 'Subcategory2'] = 'Bottomwear'
            final_df.at[ctr, 'Subcategory3'] = 'Bottomwear'
            # final_df.at[ctr, 'Url'] = f'https://api.fastsimon.com/categories_navigation?page_num=2&products_per_page=60&facets_required=1&with_product_attributes=true&request_source=v-next&src=v-next&UUID=777f83f8-820e-45d0-a08b-08c6b432b87a&uuid=777f83f8-820e-45d0-a08b-08c6b432b87a&store_id=21708465&api_type=json&narrow=%5B%5B' + f'"{attr[2]}","{attr_value[0]}"' + '%5D%5D&sort_by=relevance&category_id=193284079749'
            # final_df.at[ctr, 'Url'] = f'https://api.fastsimon.com/categories_navigation?page_num=0&products_per_page=80&facets_required=1&with_product_attributes=true&request_source=v-next&src=v-next&UUID=777f83f8-820e-45d0-a08b-08c6b432b87a&uuid=777f83f8-820e-45d0-a08b-08c6b432b87a&store_id=21708465&api_type=json&narrow=%5B%5B' + f'"{attr[2]}","{attr_value[0]}"' + '%5D%5D&sort_by=relevance&category_id=193283915909'
            # final_df.at[ctr, 'Url'] = f'https://api.fastsimon.com/categories_navigation?page_num=1&products_per_page=80&facets_required=1&with_product_attributes=true&request_source=v-next&src=v-next&UUID=777f83f8-820e-45d0-a08b-08c6b432b87a&uuid=777f83f8-820e-45d0-a08b-08c6b432b87a&store_id=21708465&api_type=json&narrow=%5B%5B' + f'"{attr[2]}","{attr_value[0]}"' + '5D%5D&sort_by=relevance&category_id=268124291205'
            final_df.at[ctr, 'Url'] = f'https://api.fastsimon.com/categories_navigation?page_num=1&products_per_page=80&facets_required=1&with_product_attributes=true&request_source=v-next&src=v-next&UUID=777f83f8-820e-45d0-a08b-08c6b432b87a&uuid=777f83f8-820e-45d0-a08b-08c6b432b87a&store_id=21708465&api_type=json&narrow=%5B' + f'"{attr[2]}","{attr_value[0]}"' + '%5D&sort_by=relevance&category_id=193283948677'
            final_df.at[ctr, 'Attr_Name'] = attr[2]
            final_df.at[ctr, 'Attr_Value'] = attr_value[0].split(':')[-1]
            ctr += 1
print(len(final_df))
final_df.to_csv('stevemadden_bottomwear_links_with_attrs.csv', index=False, index_label=False)