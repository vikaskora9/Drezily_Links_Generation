import requests
import json
import pandas as pd

response = json.loads(requests.get('https://us.shein.com/api/productList/info/get?_ver=1.1.8&_lang=en&type=entity&routeId=1727&page=1&requestType=refresh&sheinClubType=3&isPaid=0').text)
print(response)
exit()
final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value'])
tsp_data = response['filterTsps']
for attr in tsp_data:
    try:
        for attr_value in attr['tagList']:
            tmp_df = pd.DataFrame(data={'Product_Category': ['Clothing'],
                                        'Category': ['Women'],
                                        'Subcategory1': ['Western'],
                                        'Subcategory2': ['Dresses and Jumpsuits'],
                                        'Subcategory3': ['Dresses'],
                                        'Attr_Name': [''],
                                        'Attr_Value': ['']})
            tmp_df['Attr_Name'] = attr['tagGroupName']
            tmp_df['Attr_Value'] = attr_value['tagName']
            tmp_df['Url'] = f'https://us.shein.com/Women-Dresses-c-1727.html?tsp_ids={attr_value["tagId"]}'
            final_df = final_df.append(tmp_df)
    except Exception as e:
        print(attr_value['tagName'], e)
    print(len(final_df))
attr_data = response['filterAttrs']
for attr in attr_data:
    try:
        for attr_value in attr['groups']:
            tmp_df = pd.DataFrame(data={'Product_Category': ['Clothing'],
                                        'Category': ['Women'],
                                        'Subcategory1': ['Western'],
                                        'Subcategory2': ['Dresses and Jumpsuits'],
                                        'Subcategory3': ['Dresses'],
                                        'Attr_Name': [''],
                                        'Attr_Value': ['']})
            tmp_df['Attr_Name'] = attr['attr_name']
            tmp_df['Attr_Value'] = attr_value['group_name']
            # Maxi \n 54_42454
            tmp_df['Url'] = f'https://us.shein.com/Women-Dresses-c-1727.html?attr_values={attr_value["group_name"]}&attr_ids={attr_value["attr_filter"]}&exc_attr_id={attr_value["attr_id"]}'
            final_df = final_df.append(tmp_df)
    except Exception as e:
        print(attr_value['attr_name'], e)
    print(len(final_df), attr['attr_name'])
for attr in attr_data[1:]:
    try:
        for attr_value in attr['attr_values']:
            tmp_df = pd.DataFrame(data={'Product_Category': ['Clothing'],
                                        'Category': ['Women'],
                                        'Subcategory1': ['Western'],
                                        'Subcategory2': ['Dresses and Jumpsuits'],
                                        'Subcategory3': ['Dresses'],
                                        'Attr_Name': [''],
                                        'Attr_Value': ['']})
            tmp_df['Attr_Name'] = attr['attr_name']
            tmp_df['Attr_Value'] = attr_value['attr_value']
            # Maxi \n 54_42454
            tmp_df['Url'] = f'https://us.shein.com/Women-Dresses-c-1727.html?attr_values={attr_value["attr_value"]}&attr_ids={attr_value["attr_filter"]}&exc_attr_id={attr_value["attr_id"]}'
            final_df = final_df.append(tmp_df)
    except Exception as e:
        print(attr_value['attr_name'], e)
    print(len(final_df), attr['attr_name'])
final_df.to_csv('Shein_links_with_attrs.csv', index=False, index_label=False)


