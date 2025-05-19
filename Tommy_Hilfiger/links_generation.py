import requests
import pandas as pd
from bs4 import BeautifulSoup

# https://usa.tommy.com/on/demandware.store/Sites-PVHTHUS-Site/en_US/Search-ShowAjax?cgid=Folder_19514351&srule=Featured_New%20Badge&page=1
resp = BeautifulSoup(requests.get('https://usa.tommy.com/on/demandware.store/Sites-PVHTHUS-Site/en_US/Search-ShowAjax?cgid=Folder_18483053&srule=Featured_New%20Badge&start=16&sz=16&deviceType=desktop',
                                  headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15'}).text, 'html.parser')
# print(resp)
# exit()

df, ctr = pd.DataFrame(), 0
for i, data in enumerate(resp.find('div', {'class': 'refinements'}).find_all('div', {'class': 'enable-drawer'})):
    try:
        if data['id'] in ['color-drawer', 'fit-drawer', 'sleeve-length-drawer', 'neckline-drawer', 'style-drawer']:
            for data_2 in data.find('div', {'class': 'content-inner'}).find_all('div'):
                # df.at[ctr, 'Category'] = 'Women'
                # df.at[ctr, 'Product_Category'] = 'Clothing'
                # df.at[ctr, 'Subcategory1'] = 'Western'
                # df.at[ctr, 'Subcategory2'] = 'Outerwear'
                # df.at[ctr, 'Subcategory3'] = 'Sweatshirts & Sweatpants'
                # try:
                #     df.at[ctr, 'Url'] = f'https://usa.tommy.com{data_2.find("div")["data-href"]}'
                # except:
                #     try:
                #         df.at[ctr, 'Url'] = f'https://usa.tommy.com{data_2.find("a")["href"]}'
                #     except:
                #         try:
                #             df.at[ctr, 'Url'] = f'https://usa.tommy.com{data_2.find("div")["data-value"]}'
                #         except:
                #             continue
                print(data['id'].strip())
                try:
                    print(data_2.find('label')['data-displayvalue'])
                except:
                    # print(data_2)
                    continue
                df.at[ctr, 'Attr_Name'] =data['class'][1]

                if len(data_2.find('span').text.strip())>0:
                    df.at[ctr, 'Attr_Value'] = data_2.find('span').text.strip()
                else:
                    df.at[ctr, 'Attr_Value'] = data_2.find('a')['data-refinement-id'].split('-')[-1]
                ctr += 1
    except Exception as e:
        print()
        pass
    # exit()
    # continue

df.to_csv('tommy_hilfiger_dresses_filters.csv', index=False, index_label=False)