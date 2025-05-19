import requests
import json
import pandas as pd


payload = json.dumps({"query":"\n\t\t\tquery($categoryPath: String) {\n\t\t\t\tsearch(\n\t\t\t\t\taccountId: \"shopify-6186270804\"\n\t\t\t\t\tproducts: {\n\t\t\t\t\t\tcategoryPath: $categoryPath,\n\t\t\t\t\t\tsize: 48,\n\t\t\t\t\t}\n\t\t\t\t) {\n\t\t\t\t\tproducts {\n\t\t\t\t\t\tfacets {\n\t\t\t\t\t\t\t... on SearchTermsFacet {\n\t\t\t\t\t\t\t\tid\n\t\t\t\t\t\t\t\tfield\n\t\t\t\t\t\t\t\ttype\n\t\t\t\t\t\t\t\tname\n\t\t\t\t\t\t\t\tdata {\n\t\t\t\t\t\t\t\t\tvalue\n\t\t\t\t\t\t\t\t\tcount\n\t\t\t\t\t\t\t\t\tselected\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t... on SearchStatsFacet {\n\t\t\t\t\t\t\t\tid\n\t\t\t\t\t\t\t\tfield\n\t\t\t\t\t\t\t\ttype\n\t\t\t\t\t\t\t\tname\n\t\t\t\t\t\t\t\tmin\n\t\t\t\t\t\t\t\tmax\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t\ttotal\n\t\t\t\t\t\tsize\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t","variables":{"categoryPath":"Women's Graphic Tees"}})

resp = json.loads(requests.post('https://search.nosto.com/v1/graphql', data=payload).text)
# print(resp.text)
df, ind = pd.DataFrame(), 0

for i, row in enumerate(resp['data']['search']['products']['facets']):
    try:
        for data in row['data']:
            df.at[ind, 'Product_Category'] = 'Clothing'
            df.at[ind, 'Category'] = 'Women'
            df.at[ind, 'Subcategory1'] = 'Western'
            df.at[ind, 'Subcategory2'] = 'Topwear'
            df.at[ind, 'Subcategory3'] = 'T-Shirts'
            df.at[ind, 'Url'] = f'https://us.princesspolly.com/collections/graphic-tees?filter.{row["field"]}={data["value"]}'
            df.at[ind, 'Attr_Name'] = row['field']
            df.at[ind, 'Attr_Value'] = data['value']
            df.at[ind, '_id'] = json.dumps({'field': row['field'], 'value': [data['value']] })
            ind+=1
    except Exception as e:
        print(row['field'], e)

df.to_csv('PrincessPolly_T-Shirts.csv', index=False, index_label=False)