import json

import requests
from bs4 import BeautifulSoup

payload = json.dumps({
    '_ver': '1.1.8',
    '_lang': 'en',
    'type': 'entity',
    'routeId': '12472',
    'page': '4',
    'ici': 'us_tab01navbar03menu01dir05',
    'src_module': 'topcat',
    'src_identifier': 'fc=New In`sc=Women Clothing`tc=Shop by category`oc=Dresses`ps=tab01navbar03menu01dir05`jc=real_12472',
    'adp': '40660241',
    'src_tab_page_id': 'page_home1730952254870',
    'categoryJump': 'common:210937:shein:us_en:ios_!_0',
    'requestType': 'pageChange',
    'reqSheinClub': True,
    'isPaid': '0'})
response = BeautifulSoup(requests.get('https://us.shein.com/api/productList/info/get',
                                      data=payload,
                                      headers={
                                          'authority': 'us.shein.com',
                                          'method': 'GET',
                                          'Accept': 'application/json, text/plain, */*',
                                          'Accept-Encoding': 'gzip, deflate, br, zstd',
                                          'Accept-Language': 'en-US,en;q=0.9',
                                          'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
                                          'referer': 'https://us.shein.com/Women-Dresses-c-12472.html?ici=us_tab01navbar03menu01dir05&src_module=topcat&src_identifier=fc%3DNew%20In%60sc%3DWomen%20Clothing%60tc%3DShop%20by%20category%60oc%3DDresses%60ps%3Dtab01navbar03menu01dir05%60jc%3Dreal_12472&adp=40660241&src_tab_page_id=page_home1730952254870&categoryJump=common%3A210937%3Ashein%3Aus_en%3Aios_!_0&page=4',
                                          'sec-ch-ua-mobile': '?0',
                                          'sec-ch-ua-platform': 'Windows',
                                          'sec-fetch-dest': 'empty',
                                          'sec-fetch-mode': 'cors',
                                          'sec-fetch-site': 'same-origin',
                                          'smdeviceid': 'WHJMrwNw1k/EcCPAhVuCvdGn8deCGkMxHxblffPkbCko/v5Geemx3kRH33OiZRJ8AL4nV2HTYg54OWSR0kYmnqCE7bcRxPmJDdCW1tldyDzmQI99+chXEirbERY+Ro7ooU1gw1puiLgyGB6sbmT1rpQSexwDa7oQ44LLFRLThMoiRnmw+D/dfPLF8XccDmOxGrB/5gjhd/Kvq6sEop3iSw0G9BGS7GIk5J4qoUhwVsjEOeW3xefyG8MARmVqJ0utp1487582755342',
                                          'uber-trace-id': 'ff14ceebd793c873:ff14ceebd793c873:0:0',
                                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
                                          'x-csrf-token': '6nQo6VnX-Mw8K5s_PoHf2lHcCIMBtysH8jiU',
                                          'x-gw-auth': 'a=xjqHR52UWJdjKJ0x6QrCsus66rNXR9@2.0.13&b=1730955188316&d=06942fbc37be6a98b8dee877d03ae8f6&e=rk1anZThkMDFmODYwM2E2ZWEyM2QzODZmZWRhZTZjOTYxZmU0MTIwODVlYjIzOTYzYWEyZDkxYjI1MGM3YjM5NTk0Zg%3D%3D',
                                          'x-requested-with': 'XMLHttpRequest',
                                          'armortoken': 'T0_3.0.1__OVWaW2LoRA-6IbpC2IFm_PROC-rwxS9qDABf4-p48gWnWlLyn5xBJNQKQWer_PmlirKSzPydfRPi6p8MxTAMSCFW1P9n0a91TKgQKmDtGJIJ9je8lHmygH5q9ltKYZwsQNL3JBGbJ9bBiy2JL2ZJnsIO0A3MgG0SDRwCHY8eWYvGMMFE9v9CdVVTWhbUfLF_1730952270524',
                                          'anti-in': '0_1.6.2_f73d62_DqjcXtMUMNah6F_Vt28VthegdrsIP-ZQJK1XI2KX0h8LDmtx8G5XJ2JdMShqK7Vl9EXcxyinuyylmDgJ9raIOravYfjmmkU0tuNdOFnkRsYxyLGsO2xNB_3D1uflvLxEfBOsdmRvd_2SASto2RB2NkukMLfgdnRXztxFS86ECVafBs7a6CCCWmlxQ7smU8vdnU3S4rs5ONdyYmAi1Ov2DLrPdRqR3ogPb5njY3bAicCqRXDp6lLigJOlcFm0NKTgjd6GU2__Xwl8WnrWhBsYzShcWNhIOYKPxWNiKSPJmuiIt5BcuC0RYqTXvKyiCdn1tNjNEzJZ3XtV6AdUtgM6KUoINTVnGAraPTgaTU0IQjduMhUR5l00yFfj0Mtmn0k1WZ00U1DMnEbc1qjTPyCvKBvI16NrB5RtRRi6821BK7XCBnI0yylEE1Rk_aWw7n-Bs4fYkFSVaOrJACskojdweuipd0rsVNtBHcfqiOHbJP6STUqJz0Dcpt5-JmBFjfav-dL3oqHHCQ-lZY0k39UPOoShcRKAae8pSDpgsCgQy1kR2alevqOhm-siKRwlKuAM4hI73evO9KKlNIhMVEW8AUROafoTVOMrmuq2-zX-1I_nLI91cOWnvS18FUib_SJR9anICw0NxOppalNcxElH-KF4nWMmGr_0i4Ss18Iex4k4_wa9p8RJcKKIAmMZfT4GwotPBItMKgCeMNYYsIkFSadoUEsyaRcSbr2qL8h_Wvqnk9Zgv2ZiE3s1s8O52cps7glM248PLZt-LUCHvh9UDiKrZEZZfvCL_EvJWsQFw0C3RwPp7CYrG4ZbsDDn4jkiRLKsuVFmi1uT5hC6ykun3AP',
                                          'cookie': 'cookieId=47F3D6E1_845C_FFF4_4129_75091C997592; AT=MDEwMDE.eyJiIjo3LCJnIjoxNzMwOTUyMjU0LCJyIjoiN3V6VFlwIiwidCI6MX0.f902116c2f701f95; sessionID_shein=s%3ACW7O9dEfSYBiY05HQDD-fc6VP54YaRM6.Dxqko%2F2%2F4ASX178RoSjMY%2Bs7RsMp7QZjxZNKUtvKLnA; _cfuvid=EYGIxanYAQbMLMgYx.5j6vIGFIpENbM5GEW5XSzjL3w-1730952255565-0.0.1.1-604800000; RESOURCE_ADAPT_WEBP=1; cf_clearance=WkAkSQkHgdNKaf3V9_hgcHC3mWuM2.pQOC4_DZ82hNA-1730952258-1.2.1.1-5z9FUMUQNB0fUggtcJMxoTWhMD2OtVVtkYCbemHLRAblUeHN3E_exUhgvmamnaObYeIpekc65RG5v6ftDw_WmH8_m8c7eQbV4aQyKnm9IvGequRLLcOY1NpqOGOA3fLLi4hV48P4X.9HsSjNmaUWePnPp48OjKpmEMupFPpwIG2OcTvH172dpiI4JU460qvYm2f1N3_2e6epqm6Rn4szNiRwAlGgHrUNtUkBsXsSQak2Mjx0b1R7aiB0jiE7M03EqpJKZhli.RKZF7hEz.PmEObZb2biQpeDJ7DXQb5Wc0TD7ttvUHQwvGTDI2Wi2sf7oILBf6u5LvwTzHCsqZvlucBN18_Q5wGNdEo0rKpsdMyLSGs5_slIDghHbPBPAAmTSybX8Z8Rb8j9cYR6gei4LA; smidV2=202312051227088d793dcae4f94c1c234c032366cc561500442df3cf85bef80; armorUuid=202409092334501924b7132d88fa6f86ada23a06693cda00db1d117de3879600; ndp_session_id=03456417-e36d-4987-aa9d-fc746aed1623; webpushcookie=agree%3A1; _scid=NugFRNEptOTNwpojsYIgTF59wc21XMaKfHo9iw; _scid_r=NugFRNEptOTNwpojsYIgTF59wc21XMaKfHo9iw; _uetsid=675739e09cbd11efb8cbdd663f3e1707; _uetvid=887243b0933b11eeaff7dd84072b2609; _ScCbts=%5B%5D; _gcl_au=1.1.1551675717.1730952277; _pin_unauth=dWlkPU1tUTRObVZoTkdNdFpXTXhZaTAwWVdKbExUaGxNakF0WkdabU1HTmhNall3WkRsaA; cto_bundle=PaSkmV9KJTJCUFIxYkYxZ2hmWmRRRXU3TDV5JTJGN1N1emRPdnlXZFlDcUNmU1k4ZyUyRkRUcXRvTFlYR2tJZ2JxeGp2R1FRaU9uTmd1SEFFamozMThRaVJ0cWY0RGVMZFdxclk0TmtEM3FwRmRsZHZoeFZTc3c2TFFKSm4yMXF1SmxmdEd2UVpITmNsRDh5MHNiTTZUcyUyQlplbGtpMFU1ZyUzRCUzRA; _fbp=fb.1.1730952278648.860718180422354858; _sctr=1%7C1730917800000; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Nov+07+2024+10%3A16%3A52+GMT%2B0530+(India+Standard+Time)&version=202311.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0520795f-7cc3-4835-bb40-bac510469035&interactionCount=0&landingPath=https%3A%2F%2Fus.shein.com%2FWomen-Dresses-c-12472.html%3Fici%3Dus_tab01navbar03menu01dir05%26src_module%3Dtopcat%26src_identifier%3Dfc%253DNew%2520In%2560sc%253DWomen%2520Clothing%2560tc%253DShop%2520by%2520category%2560oc%253DDresses%2560ps%253Dtab01navbar03menu01dir05%2560jc%253Dreal_12472%26adp%3D40660241%26src_tab_page_id%3Dpage_home1730952254870%26categoryJump%3Dcommon%253A210937%253Ashein%253Aus_en%253Aios_!_0%26page%3D3&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0005%3A0%2CC0004%3A0; _rdt_uuid=1730952274807.015c1251-d825-440b-bb7d-749bbd17ca41',
                                          'priority': 'u=1, i'
                                          # 'authority': 'www.torrid.com',
                                          # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
                                      }
                                      ).text,
                         'html.parser')
print(response)
# print('=----------------------break-----------------------=')
exit()
# og_link :- https://www.torrid.com/product/mini-poplin-top-ponte-bustier-shirt-dress/41275171-05026.html?cgid=Clothing_Dresses
prod_response = BeautifulSoup(requests.get(
    'https://www.torrid.com/on/demandware.store/Sites-torrid-Site/default/Product-Variation?pid=41275171-05026&dwvar_41275171-05026_color=BLACK%20WHITE&cgid=Clothing_Dresses&Quantity=1&format=ajax&setQty=true&bonusDiscountLineItemUUID=',
    headers={
        'method': 'GET',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'authority': 'www.torrid.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}).text,
                              'html.parser')
# print(prod_response)

revolve_desc = BeautifulSoup(requests.get(
    'https://www.revolve.com/lacademie-ashleigh-stretch-cotton-cargo-mini-dress-in-khaki-beige/dp/LCDE-WD721/',
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}).text,
                             'html.parser')
print(revolve_desc)
