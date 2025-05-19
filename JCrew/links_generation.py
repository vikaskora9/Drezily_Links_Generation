import requests
import pandas as pd
import json
from copy import deepcopy

resp = requests.get('https://www.jcrew.com/browse/product_search?expand=variations%2Cavailability&count=60&start=60&refine=cgid%3Dwomens%7Ccategories%7Cclothing%7Cshirts-and-tops&refine_1=c_allowedCountries%3DALL%7CUS&refine_2=c_displayOn%3Dstandard_usd&refine_3=isAppExclusive%3Dfalse&country-code=US&seo-word-cloud-key=%2Fwomens%2Fcategories%2Fclothing%2Fshirts-and-tops')
#
# resp_json = json.loads(resp.text)

final_df = pd.DataFrame()
# valid_attr_lst = ['Color', 'Pattern', '7::Fabric', '2::Length', '6::Silhouette', '1::Occasion']
ctr = 0
attr_lst = json.loads(resp.text)['refinements']
for attr in attr_lst:
    # if attr['label'] in valid_attr_lst:
        print(attr['label'], attr['attribute_id'])
        # continue
        try:
            for attr_value in attr['values']:
                final_df.at[ctr, 'Product_Category'] = 'Clothing'
                final_df.at[ctr, 'Category'] = 'Women'
                final_df.at[ctr, 'Subcategory1'] = 'Western'
                final_df.at[ctr, 'Subcategory2'] = 'Topwear'
                final_df.at[ctr, 'Subcategory3'] = 'Topwear'
                # https://www.jcrew.com/browse/product_search?expand=variations%2Cavailability&count=60&start=0&refine=c_allowedCountries%3DALL%7CUS&refine_1=c_displayOn%3Dstandard_usd&
                # refine_2=&refine_3=isAppExclusive%3Dfalse&country-code=US&seo-word-cloud-key=&refine_2=&refine_3=isAppExclusive%3Dfalse&country-code=US&seo-word-cloud-key=
                final_df.at[ctr, 'Url'] = f'https://www.jcrew.com/browse/product_search?expand=variations%2Cavailability&count=60&start=0&refine=c_allowedCountries%3DALL%7CUS&refine_1=c_displayOn%3Dstandard_usd' \
                                        f'refine_2={attr["attribute_id"]}%3D{attr_value["label"]}&refine_3=cgid%3Dwomens%7Ccategories%7Cclothing%7Cshirts-and-tops&refine_4=isAppExclusive%3Dfalse&country-code=US' \
                                        f'&seo-word-cloud-key=%2Fwomens%2Fcategories%2Fclothing%2Fshirts-and-tops%2F{attr["label"].lower()}%3D{attr_value["label"]}'
                final_df.at[ctr, 'Attr_Name'] = attr['label']
                try:
                    final_df.at[ctr, 'Attr_Value'] = attr_value['description']
                except:
                    final_df.at[ctr, 'Attr_Value'] = attr_value['value']
                final_df.at[ctr, 'Counts'] = attr_value['hit_count']
                ctr += 1
        except:
             print(attr)
print(len(final_df))
final_df.to_csv('JCrew_topwear_3.csv', index=False, index_label=False)