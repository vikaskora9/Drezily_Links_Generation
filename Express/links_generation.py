import json
from bs4 import BeautifulSoup
import pandas as pd
import requests


params = {"operationName":"getUnbxdCategory","variables":{"categoryId":"cat550007","filter":"occasion_uFilter:Cocktail & Party","overrideCatApi":"","rows":56,"sort":"","start":0,"queryParams":[],"queryName":"getUnbxdCategory"},"query":"query CategoryQuery($categoryId: String, $start: Int!, $rows: Int, $filter: String, $sort: String, $overrideCatApi: String, $uc_param: String, $queryParams: [String]) {\n  getUnbxdCategory(categoryId: $categoryId, start: $start, rows: $rows, filter: $filter, sort: $sort, overrideCatApi: $overrideCatApi, uc_param: $uc_param, queryParams: $queryParams) {\n    categoryId\n    categoryName\n    facets {\n      facetId\n      name\n      position\n      values\n      valuesWithCount {\n        value\n        count\n        __typename\n      }\n      __typename\n    }\n    pagination {\n      totalProductCount\n      pageNumber\n      pageSize\n      start\n      end\n      __typename\n    }\n    products {\n      availabilityStoreIds\n      averageOverallRating\n      colors {\n        color\n        skuUpc\n        defaultSku\n        defaultSkuUpc\n        imageSet\n        colorFamily\n        __typename\n      }\n      EFOProduct\n      ensembleListPrice\n      ensembleSalePrice\n      key\n      isEnsemble\n      listPrice\n      marketplaceProduct\n      name\n      newProduct\n      onlineExclusive\n      onlineExclusivePromoMsg\n      paginationEnd\n      paginationStart\n      productDescription\n      productId\n      productImage\n      productURL\n      promoArray {\n        ensembleItem\n        promoMessage\n        __typename\n      }\n      promoMessage\n      salePrice\n      totalReviewCount\n      __typename\n    }\n    requestId\n    source\n    sortAlgorithm {\n      sortParamSource\n      algorithm\n      otherSortParams\n      __typename\n    }\n    __typename\n  }\n}\n",
          "MIME Type": "application/json"}
prods = BeautifulSoup(requests.post('https://www.express.com/graphql',
                    headers={
                                                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
"method": "POST",
"scheme": "https",
"authority": "www.express.com",
"path": "/graphql",
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9",
"Connection": "keep-alive",
"Content-Length": "1809",
"Content-Type": "application/json",
"Host": "www.express.com",
"Origin": "https://www.express.com",
"Referer": "https://www.express.com/womens-clothing/dresses/cat550007/filter/occasion_uFilter:Cocktail%20%26%20Party?ICID=TN_W_DRESSES_DRESSSHOP",
"Content-Type": "application/json",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"X-EXP-REQUEST-ID": "77d27fc9-e02e-4cb7-959d-5b14c3aee9ca",
"X-EXP-RVN-CACHE-KEY": "b1a7650cd9b6ffcc64a212943c025c0f0b83ce1051188c5d146466b8e65175a4",
"X-EXP-RVN-CACHEABLE": "true",
"X-EXP-RVN-QUERY-CLASSIFICATION": "getUnbxdCategory",
"X-EXP-RVN-SOURCE": "app_express.com",
},
                    data=params
                    ).text, 'html.parser')

json_data = json.loads(prods.text)
print(json_data['data']['getUnbxdCategory']['pagination']['totalProductCount'])
exit()
df = pd.DataFrame()
ctr = 0
for facet in json_data['data']['getUnbxdCategory']['facets']:
    for facets_2 in facet['values']:
        df.at[ctr, 'Product_Category'] = 'Clothing'
        df.at[ctr, 'Category'] = 'Women'
        df.at[ctr, 'Subcategory1'] = 'Western'
        df.at[ctr, 'Subcategory2'] = 'Dresses and Jumpsuits'
        df.at[ctr, 'Subcategory3'] = 'Dresses'
        df.at[ctr, 'Url'] = f"https://www.express.com/womens-clothing/dresses/cat550007/filter/{facet['facetId']}:{facets_2}?ICID=TN_W_DRESSES_ALL"
        df.at[ctr, '_id'] = f"{facet['facetId']}:{facets_2}"
        df.at[ctr, 'Attr_Name'] = facet['facetId']
        df.at[ctr, 'Attr_Value'] = facets_2
        ctr+=1

df.to_csv('Dresses_facets.csv', index=False, index_label=False)