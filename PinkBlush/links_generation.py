from copy import deepcopy

import pandas as pd
import requests
import json


df = pd.read_csv('/Users/shardakora/Desktop/Drezily_Scrapypoet/scrapyPageObjects/spiders/pages/Pinkblush_Maternity/Women/links.csv')
final_df = pd.DataFrame()
for i, row in df.iterrows():
    attr_lst = json.loads(requests.get(row['Url']).text)['facets'][4:]
    for all_attr in attr_lst:

        for attr_value in all_attr['values']:
            tmp_df = pd.DataFrame(deepcopy(row))
            print(tmp_df)
            facet_attr_name = all_attr['field']
            attr_label = all_attr['label'].replace(' ', '_')
            if attr_label == 'Material':
                attr_label = 'Fabric'
            tmp_df['Attr_Name'] = attr_label
            tmp_df['Attr_Value'] = attr_value['value']
            print(tmp_df)
            tmp_df['Url'] = tmp_df['Url'].replace('&bgfilter', f'&filter.{facet_attr_name}={attr_value["value"]}&bgfilter')
            final_df = pd.concat([final_df, pd.Series(tmp_df)], ignore_index=True)
    print(len(final_df))
final_df.to_csv('pinkblush_links_shirts.csv', index=False, index_label=False)