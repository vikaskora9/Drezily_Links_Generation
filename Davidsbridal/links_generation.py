import traceback
import warnings
warnings.filterwarnings("ignore")
from copy import deepcopy
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
# initial link:- https://www.davidsbridal.com/api/graphql?query=query+getCategoryProducts%28%24pageSize%3AInt%21%24currentPage%3AInt%21%24filters%3AProductAttributeFilterInput%21%24sort%3AProductAttributeSortInput%29%7Bproducts%28pageSize%3A%24pageSize+currentPage%3A%24currentPage+filter%3A%24filters+sort%3A%24sort%29%7Bitems%7B__typename+id+...ProductDataFragment+price_range%7B...PriceRangeFragment+__typename%7Dvariant_index_data%7Bvariants%7B...VariantIndexData+__typename%7Dcount+__typename%7D...on+ConfigurableProduct%7Bis_guarantee_in_stock+__typename%7D%7Dpage_info%7Btotal_pages+__typename%7Dtotal_count+__typename%7D%7Dfragment+ProductDataFragment+on+ConfigurableProduct%7Bid+sku+uuid+name+full_url_path+facet_brand+facet_brand_value+facet_availability+facet_channel_availability+facet_subtype+descriptive_image+is_badge_coming_soon+is_pricing_final_sale+is_badge_sample_sale+is_badge_special_value+descriptive_department_id+__typename%7Dfragment+PriceRangeFragment+on+PriceRange%7Bminimum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7Dmaximum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7D__typename%7Dfragment+VariantIndexData+on+VariantIndexItemDataV2%7Bcolor_id+hex_code+image+is_default+__typename%7D&operationName=getCategoryProducts&variables=%7B%22currentPage%22%3A1%2C%22filters%22%3A%7B%22                                                   category_id%22%3A%7B%22eq%22%3A%22312%22%7D%2C%22price%22%3A%7B%7D%7D%2C%22pageSize%22%3A1000%2C%22sort%22%3A%7B%22position%22%3A%22ASC%22%7D%7D
# after filter:- https://www.davidsbridal.com/api/graphql?query=query+getCategoryProducts%28%24pageSize%3AInt%21%24currentPage%3AInt%21%24filters%3AProductAttributeFilterInput%21%24sort%3AProductAttributeSortInput%29%7Bproducts%28pageSize%3A%24pageSize+currentPage%3A%24currentPage+filter%3A%24filters+sort%3A%24sort%29%7Bitems%7B__typename+id+...ProductDataFragment+price_range%7B...PriceRangeFragment+__typename%7Dvariant_index_data%7Bvariants%7B...VariantIndexData+__typename%7Dcount+__typename%7D...on+ConfigurableProduct%7Bis_guarantee_in_stock+__typename%7D%7Dpage_info%7Btotal_pages+__typename%7Dtotal_count+__typename%7D%7Dfragment+ProductDataFragment+on+ConfigurableProduct%7Bid+sku+uuid+name+full_url_path+facet_brand+facet_brand_value+facet_availability+facet_channel_availability+facet_subtype+descriptive_image+is_badge_coming_soon+is_pricing_final_sale+is_badge_sample_sale+is_badge_special_value+descriptive_department_id+__typename%7Dfragment+PriceRangeFragment+on+PriceRange%7Bminimum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7Dmaximum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7D__typename%7Dfragment+VariantIndexData+on+VariantIndexItemDataV2%7Bcolor_id+hex_code+image+is_default+__typename%7D&operationName=getCategoryProducts&variables=%7B%22currentPage%22%3A1%2C%22filters%22%3A%7B%22facet_length%22%3A%7B%22eq%22%3A%221763%22%7D%2C%22category_id%22%3A%7B%22eq%22%3A%22282%22%7D%2C%22price%22%3A%7B%7D%7D%2C%22pageSize%22%3A24%2C%22sort%22%3A%7B%22position%22%3A%22ASC%22%7D%7D
# color filter:- https://www.davidsbridal.com/api/graphql?query=query+getCategoryProducts%28%24pageSize%3AInt%21%24currentPage%3AInt%21%24filters%3AProductAttributeFilterInput%21%24sort%3AProductAttributeSortInput%29%7Bproducts%28pageSize%3A%24pageSize+currentPage%3A%24currentPage+filter%3A%24filters+sort%3A%24sort%29%7Bitems%7B__typename+id+...ProductDataFragment+price_range%7B...PriceRangeFragment+__typename%7Dvariant_index_data%7Bvariants%7B...VariantIndexData+__typename%7Dcount+__typename%7D...on+ConfigurableProduct%7Bis_guarantee_in_stock+__typename%7D%7Dpage_info%7Btotal_pages+__typename%7Dtotal_count+__typename%7D%7Dfragment+ProductDataFragment+on+ConfigurableProduct%7Bid+sku+uuid+name+full_url_path+facet_brand+facet_brand_value+facet_availability+facet_channel_availability+facet_subtype+descriptive_image+is_badge_coming_soon+is_pricing_final_sale+is_badge_sample_sale+is_badge_special_value+descriptive_department_id+__typename%7Dfragment+PriceRangeFragment+on+PriceRange%7Bminimum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7Dmaximum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7D__typename%7Dfragment+VariantIndexData+on+VariantIndexItemDataV2%7Bcolor_id+hex_code+image+is_default+__typename%7D&operationName=getCategoryProducts&variables=%7B%22currentPage%22%3A1%2C%22filters%22%3A%7B%22defining_color%22%3A%7B%22in%22%3A%5B%22429%22%2C%22255%22%2C%229321%22%2C%22692%22%2C%221231%22%5D%7D%2C%22category_id%22%3A%7B%22eq%22%3A%22282%22%7D%2C%22price%22%3A%7B%7D%7D%2C%22pageSize%22%3A24%2C%22sort%22%3A%7B%22position%22%3A%22ASC%22%7D%7D
# filters%22%3A%7B%22
# df = pd.read_csv('C:/Users/vikas/PycharmProjects/Scrapypoet/scrapyPageObjects/spiders/pages/Shopbop/Women/links.csv')
final_df = pd.DataFrame(columns=['Attr_Name', 'Attr_Value'])

attr_lst = json.loads(BeautifulSoup(requests.get('https://www.davidsbridal.com/dresses/all-dresses',
                                   headers={
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
                                   #     'path': '/commerce/search/products/v2/cc?brand=on&market=us&cid=15292&locale=en_US&pageSize=300&ignoreInventory=false&includeMarketingFlagsDetails=true&pageNumber=1&vendor=Certona&trackingid=806429477362237',
                                   #     'scheme': 'https',
                                   #     'Accept': '*/*',
                                   #     'Accept-Encoding': 'gzip, deflate, br',
                                   #     'Accept-Language': 'en-US,en;q=0.9',
                                   #     'Origin': 'https://oldnavy.gap.com',
                                   #     'Referer': 'https://oldnavy.gap.com/',
                                   #     'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"'
                                   }
                                   ).text, 'html.parser').find('script', {'id': '__NEXT_DATA__'}).text)
# print(attr_lst['props']['pageProps']['__APOLLO_STATE__']['ROOT_QUERY']['products({"filter":{"category_id":{"eq":"282"}}})']['aggregations'])
for attr in attr_lst['props']['pageProps']['__APOLLO_STATE__']['ROOT_QUERY']['products({"filter":{"category_id":{"eq":"282"}}})']['aggregations']:
    try:
        print(attr['attribute_code'])
        try:
            for attr_value in attr['group_options']:
                if attr['attribute_code'] == 'defining_color':
                    # print()
                    # exit()
                # continue
                    tmp_df = pd.DataFrame(data={
                        # 'Product_Category': ['Clothing'],
                        #                     'Category': ['Women'],
                        #                     'Subcategory1': ['Western'],
                        #                     'Subcategory2': ['Dresses and Jumpsuits'],
                        #                     'Subcategory3': ['Dresses'],
                                            'Attr_Name': [''],
                                            'Attr_Value': ['']})
                    tmp_df['Attr_Name'] = 'Color'
                    tmp_df['Attr_Value'] = attr_value['label']
                    col_value = '%5B'
                    ctr = 1
                    # print(len(attr_value['options']))
                    for col_code in attr_value['options']:

                        if ctr < len(attr_value['options']):
                            col_value += f'%22{col_code["value"]}%22%2C'
                            ctr+=1
                        else: col_value += f'%22{col_code["value"]}%22'
                    col_value += '%5D'
                    # exit()
                    # tmp_df[
                    #     'Url'] = f"https://www.davidsbridal.com/api/graphql?query=query+getCategoryProducts%28%24pageSize%3AInt%21%24currentPage%3AInt%21%24filters%3AProductAttributeFilterInput%21%24sort%3AProductAttributeSortInput%29%7Bproducts%28pageSize%3A%24pageSize+currentPage%3A%24currentPage+filter%3A%24filters+sort%3A%24sort%29%7Bitems%7B__typename+id+...ProductDataFragment+price_range%7B...PriceRangeFragment+__typename%7Dvariant_index_data%7Bvariants%7B...VariantIndexData+is_new_color+__typename%7Dcount+__typename%7Dis_facet_new_arrival+is_new_arrival+is_new_color_added+review_rate+review_count+facet_convertible_value+...on+ConfigurableProduct%7Bis_guarantee_in_stock+__typename%7D...on+VirtualProduct%7Bespot_image+espot_link+__typename%7D%7Dpage_info%7Btotal_pages+__typename%7Dtotal_count+__typename%7D%7Dfragment+ProductDataFragment+on+ConfigurableProduct%7Bid+sku+uuid+name+full_url_path+facet_brand+facet_brand_value+facet_availability+facet_channel_availability+facet_subtype+descriptive_image+is_badge_coming_soon+is_pricing_final_sale+is_badge_sample_sale+is_badge_special_value+is_facet_new_arrival+is_new_arrival+is_new_color_added+descriptive_department_id+__typename%7Dfragment+PriceRangeFragment+on+PriceRange%7Bminimum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7Dmaximum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7D__typename%7Dfragment+VariantIndexData+on+VariantIndexItemDataV2%7Bcolor_id+hex_code+image+is_default+category_use+__typename%7D&operationName=getCategoryProducts&variables=%7B%22currentPage%22%3A1%2C%22filters%22%3A%7B%22{attr['attribute_code']}%22%3A%7B%22in%22%3A{col_value}%7D%2C%22category_id%22%3A%7B%22eq%22%3A%22282%22%7D%2C%22price%22%3A%7B%7D%7D%2C%22pageSize%22%3A24%2C%22sort%22%3A%7B%22position%22%3A%22ASC%22%7D%7D"
                    final_df = final_df.append(tmp_df)
        except:

            for attr_v2 in attr['options']:
                tmp_df = pd.DataFrame(data={'Attr_Name': [''],
                                            'Attr_Value': ['']})
                print(attr['label'],attr_v2['label'])
                tmp_df['Attr_Name'] = attr['label']
                tmp_df['Attr_Value'] = attr_v2['label']
    #         tmp_df['Url'] = f'https://www.davidsbridal.com/api/graphql?query=query+getCategoryProducts%28%24pageSize%3AInt%21%24currentPage%3AInt%21%24filters%3AProductAttributeFilterInput%21%24sort%3AProductAttributeSortInput%29%7Bproducts%28pageSize%3A%24pageSize+currentPage%3A%24currentPage+filter%3A%24filters+sort%3A%24sort%29%7Bitems%7B__typename+id+...ProductDataFragment+price_range%7B...PriceRangeFragment+__typename%7Dvariant_index_data%7Bvariants%7B...VariantIndexData+__typename%7Dcount+__typename%7D...on+ConfigurableProduct%7Bis_guarantee_in_stock+__typename%7D%7Dpage_info%7Btotal_pages+__typename%7Dtotal_count+__typename%7D%7Dfragment+ProductDataFragment+on+ConfigurableProduct%7Bid+sku+uuid+name+full_url_path+facet_brand+facet_brand_value+facet_availability+facet_channel_availability+facet_subtype+descriptive_image+is_badge_coming_soon+is_pricing_final_sale+is_badge_sample_sale+is_badge_special_value+descriptive_department_id+__typename%7Dfragment+PriceRangeFragment+on+PriceRange%7Bminimum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7Dmaximum_price%7Bfinal_price%7Bcurrency+value+__typename%7Dregular_price%7Bcurrency+value+__typename%7Dmember_price%7Bcurrency+value+__typename%7D__typename%7D__typename%7Dfragment+VariantIndexData+on+VariantIndexItemDataV2%7Bcolor_id+hex_code+image+is_default+__typename%7D&operationName=getCategoryProducts&variables=%7B%22currentPage%22%3A1%2C%22filters%22%3A%7B%22{attr["attribute_code"]}%22%3A%7B%22eq%22%3A%22{attr_value["value"]}%22%7D%2C%22category_id%22%3A%7B%22eq%22%3A%22312%22%7D%2C%22price%22%3A%7B%7D%7D%2C%22pageSize%22%3A10%2C%22sort%22%3A%7B%22position%22%3A%22ASC%22%7D%7D'
                final_df = final_df.append(tmp_df)
    except Exception as e:
        print(attr_value['label'], traceback.format_exc())
    print(len(final_df))
final_df.to_csv('Davdisbridal_filter.csv', index=False, index_label=False)
