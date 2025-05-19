from copy import deepcopy

import pandas as pd
import requests
import json

from bs4 import BeautifulSoup

resp = requests.get('https://www.italist.com/api/search_products/61?categories[]=61&skip=0&langIsoCode2=en',
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
                        'authority': 'www.italist.com',
                        'method': 'GET',
                        'path':'/api/search_products/women?skip=1800&categories[]=64',
                        'scheme': 'https',
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br, zstd',
                        'accept-language': 'en-US,en;q=0.9',
                        'priority': 'u=1, i',
                        'cookie': 'ph_phc_oeRVOcZlhfojtNw2m06IPU3NyvNSfLF7oVOkHA2y1yq_posthog=%7B%22distinct_id%22%3A%220194fe88-918f-71e8-8ec3-a2aeb436c404%22%2C%22%24sesid%22%3A%5B1741744739753%2C%2201958811-04c1-7bc6-98e5-9043d3fdb555%22%2C1741744571585%5D%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fwww.italist.com%2Fin%2F%22%7D%7D; _dd_s=logs=1&id=ece04689-0088-4897-8948-102deeb75d88&created=1741744588161&expire=1741745639746; _ga_EM2DP8FK9T=GS1.1.1741744570.3.1.1741744707.60.0.42942568; _fbp=fb.1.1741744594950.406826525266407375; mcforms-30397519-sessionId="a2218205-4ab3-4b11-9fb7-557c1823348b"; __cuid=a4173a662b9849ed8a9b7b4d5151e6f2; _ga=GA1.1.1320062825.1741356948; _pin_unauth=dWlkPU1HUXpPRFppWlRJdFltWXhZaTAwTXpsbExUZzFZVFF0TW1FNE5ETmxOVFEyT0dNMA; _rdt_uuid=1741356952704.7fc64df1-7363-48cc-8c6c-36197eb803c7; italistsession-v2=s%3Ab198da02-d40e-443c-a16c-7bf4a2a36717.z0ufbsv4FhrfVW583Nnbueg99jP3DMPXuinRa%2FUcG1o; __kla_id=eyJjaWQiOiJORGN5WXpCak9ETXROR1EwTUMwMFlqTXpMVGt6TVRNdE4yVmhZak5pTkdKbU4yWTIiLCIkcmVmZXJyZXIiOnsidHMiOjE3Mzk0MzcxNTMsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lml0YWxpc3QuY29tL2luLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTc0MTc0NDU3NCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuaXRhbGlzdC5jb20vdXMvIn19; sbx_s1148=y; visit_s1148=ok; _gcl_au=1.1.489505395.1739437152; rCookie=ftc9e2pjndn3n7qizq74nzm733yyd6; lastRskxRun=1741356960124; rskxRunCookie=0; prov1148=a%3A4%3A%7Bi%3A1%3Bs%3A11%3A%22linkshareuk%22%3Bi%3A2%3Bs%3A4%3A%22feed%22%3Bi%3A3%3Bs%3A0%3A%22%22%3Bi%3A4%3Bs%3A0%3A%22%22%3B%7D; my-italist-feature-announcement=seen',
                        'referer': 'https://www.italist.com/us/women/clothing/dresses/13/',
                        'sec-ch-ua': '"Microsoft Edge";v = "129", "Not=A?Brand";v = "8", "Chromium";v = "129"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': "Windows",
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin'})
# print(resp.text)
api_res = json.loads(resp.text)
print(api_res.keys())
# exit()

final_df = pd.DataFrame(columns=['Product_Category','Category','Subcategory1','Subcategory2','Subcategory3','Url', 'Attr_Name', 'Attr_Value'])
ctr = 0
valid_attr_list = ['colors', 'sleeveLengths', 'seasons','onSale']

for attr in api_res['filterSettings']:
    if attr in valid_attr_list:
        print(attr)
        for attr_value in api_res['filterSettings'][attr]:
            final_df.at[ctr, 'Product_Category'] = 'Clothing'
            final_df.at[ctr, 'Category'] = 'Women'
            final_df.at[ctr, 'Subcategory1'] = 'Western'
            final_df.at[ctr, 'Subcategory2'] = 'Topwear'
            final_df.at[ctr, 'Subcategory3'] = 'T-Shirts'
            # final_df.at[ctr, 'Url'] = f'https://www.italist.com/api/search_products/women?skip=0&{attr}[]={attr_value}&categories[]=59&categories[]=44'
            final_df.at[ctr, 'Url'] = f'https://www.italist.com/api/search_products/women?skip=0&{attr}[]={attr_value}&categories[]=61'
            # final_df.at[ctr, 'Url'] = f'https://www.italist.com/api/search_products/women?skip=0&{attr}[]={attr_value}&categories[]=57&langIsoCode2=en'
            # final_df.at[ctr, 'Url'] = f'https://www.italist.com/api/search_products/59?skip=0&{attr}[]={attr_value}&categories[]=59'
            try:
                final_df.at[ctr, 'Attr_Name'] = attr

                final_df.at[ctr, 'Attr_Value'] = attr_value.title()
                ctr += 1
            except Exception as e:
                print(attr_value, e)


final_df.to_csv('italist_t-shirts_with_attrs.csv', index=False, index_label=False)