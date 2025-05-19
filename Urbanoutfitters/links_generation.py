# https://api.urbanoutfitters.com/api/catalog-search-service/v0/uo-us/tiles/dresses

import requests
import json
import pandas as pd


def get_token():
    payload = json.dumps({
        "reauthToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTc0NTM0Njc4My4yMTUxMjE3LCJpYXQiOjE3Mjk3OTQ3ODMuMjE1MTIxNywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjk3OTQ3ODMuMjE1MTA1OCwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJ0cmFjZXJcIjogXCJCQU1EVEZJNTlNXCIsIFwicHJvZmlsZUlkXCI6IFwiOVR4S3BFZG5JdW5FSk1uZFVodGpjeDNoWXNTVCtsVnpvMUVSU2tCc09qd3Z1eE5QazZKRk03dDY3a0ZveHpjcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTYxMDQ2YWNlNGEzN2YxYmJlY2FjNGFlNmMwNGYxOWE0YTQ0Yzg2MjU1YjU1MTlmZmJlNDZmMjQ2ZDI3ZjM1OGJcIn0ifQ.vVEm0QNtyicRMEd5eiVLiX8AiirBBvllP6UoSAVpub0"})

    token = json.loads(requests.put('https://www.urbanoutfitters.com/slipstream/api/token/v0/uo-us/auth',
                                    headers={'accept': 'application/json, text/plain, */*',
                                             'accept-encoding': 'gzip, deflate, br, zstd',
                                             'accept-language': 'en-US,en;q=0.9',
                                             'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcyOTc5MzgwNS4xODA2NTM4LCJpYXQiOjE3Mjk3OTMyMDUuMTgwNjUzOCwiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjc4MzczNzkuMDcyMTEwNywgXCJwcm9maWxlSWRcIjogXCI5VHhLcEVkbkl1bkVKTW5kVWh0amN4M2hZc1NUK2xWem8xRVJTa0JzT2p3dnV4TlBrNkpGTTd0NjdrRm94emNyNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09NjEwNDZhY2U0YTM3ZjFiYmVjYWM0YWU2YzA0ZjE5YTRhNDRjODYyNTViNTUxOWZmYmU0NmYyNDZkMjdmMzU4YlwiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIkJBTURURkk1OU1cIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJBUy1TR1wiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiTUhcIn0sIFwiY2FydElkXCI6IFwiYkFIeDExU0JlcVd4d3pXNGJZWlp4Y3F2TndGUE1lSUdSVFA2NkwrM1ZCUlZid1FKb2c0dFUzVGd0ZnVydEhVMTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTUxOGVkOGU0ZjhiZDhjZGI2YzhkZTU2Y2M1YmJiZjk0ZjBhOWY5NzhmYzBhOGUwNDk5ZjY3ZTUxNDM3ZDc4NGJcIn0ifQ.B9O-14pfBcwePw9GqMIVv5j-r3Sbw-fkPK3jN_ProwQ',
                                             'connection': 'keep-alive',
                                             'content-length': '541',
                                             'content-type': 'application/json',
                                             'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                                             'sec-ch-ua-mobile': '?0',
                                             'sec-ch-ua-platform': "Windows",
                                             'sec-fetch-dest': 'empty',
                                             'sec-fetch-mode': 'cors',
                                             'sec-fetch-site': 'same-origin',
                                             'x-urbn-channel': 'web',
                                             'x-urbn-country': 'IN',
                                             'x-urbn-currency': 'USD',
                                             'x-urbn-experience': 'ss',
                                             'x-urbn-geo-region': 'AS-SG',
                                             'x-urbn-language': 'en-US',
                                             'x-urbn-primary-data-center-id': 'US-NV',
                                             'x-urbn-site-id': 'uo-us',
                                             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
                                             'cookie': 'SSLB=1; urbn_site_id=uo-us; urbn_edgescape_site_id=uo-us; urbn_language=en-US; urbn_uuid=4ca70fba-632a-4f41-8bfb-a3d4fa011b70; urbn_channel=web; urbn_geo_region=AS-SG; siteId=uo-us; urbn_inventory_pool=INTL_DIRECT; urbn_tracer=BAMDTFI59M; urbn_currency=USD; urbn_country=IN; urbn_data_center_id=US-NV; urbn_device_info=web%7Cother%7Cdesktop; pxcts=f9713cae-8068-11ef-b763-c795d5131f7a; _pxvid=f78f8421-8068-11ef-9605-4d9dbd186e73; __pxvid=fa9e6192-8068-11ef-a45f-0242ac120003; cebs=1; _ga=GA1.1.178813237.1727837389; utag_main_v_id=01924b22455a000235b07ff6d5cc0507d0020075007e8; _gcl_au=1.1.1539530721.1727837391; __attentive_id=14f399d136e147168b6acc0444566215; _attn_=eyJ1Ijoie1wiY29cIjoxNzI3ODM3MzkyNTUyLFwidW9cIjoxNzI3ODM3MzkyNTUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjE0ZjM5OWQxMzZlMTQ3MTY4YjZhY2MwNDQ0NTY2MjE1XCJ9In0=; __attentive_cco=1727837392557; smartDash=8e3012a1-84a7-49ef-98d0-77d9aa9b369c; _scid=b-0F8vRovPhmY38sX9lmdnLywXxMyFDA; _pin_unauth=dWlkPVl6TXlPRFpoWXpFdE1XVTVNQzAwWXpKaExXRmlOV1V0TTJZMFlqazVORFl5TVRrdw; _fbp=fb.1.1727837394581.212925117775355125; _tt_enable_cookie=1; _ttp=L2-3ukyGvcQCAiotwjY0FEcHdjb; smartDashLRX=000; __adroll_fpc=71e8e77344487dcb3d0a7a07eb5e75dc-1727837396847; _li_dcdm_c=.urbanoutfitters.com; _lc2_fpi=18c6eee2a756--01j95j4rr5j2ayenjxzvxgnqb2; _ScCbts=%5B%5D; BVBRANDID=f696e4e8-652f-442f-b6e5-94ecc11b6b0c; ss-enable-bisn-confirmation=1; SS_SHOP_THE_LOOK_VARIANT=0; SSID=CQB48x0qAAQAAADCtPxmaseAEMK0_GYDAAAAAACDkyVnVwX-ZgAU-TlNAQFzCikAVwX-ZgEAvEwBA3n-KADCtPxmAwAWSwEDC90oAFcF_mYBALNDAQA; SSSC=472.G7421005031593265002.3|84758.2678027:85180.2686585:85305.2689651; urbn_uuid_session=eaa440f6-0b76-4ce8-a66f-22dc5b98559c; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Oct+03+2024+08%3A16%3A25+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=4ca70fba-632a-4f41-8bfb-a3d4fa011b70&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.urbanoutfitters.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; utag_main__sn=3; utag_main_ses_id=1727923587061%3Bexp-session; utag_main__pn=1%3Bexp-session; utag_main_isLoggedIn=false%3Bexp-session; utag_main_dc_visit=3; utag_main_dc_region=ap-east-1%3Bexp-session; _clck=2ammpq%7C2%7Cfpp%7C0%7C1736; _rdt_uuid=1727837392751.5e599515-0526-407a-b9a7-a9379cbffd05; _scid_r=bG0F8vRovPhmY38sX9lmdnLywXxMyFDAGsFzuQ; __ar_v4=TLGS2MDMOFEALNQLHLTLBW%3A20241001%3A6%7CQWC5THA5TZFOLOWWLOOPBD%3A20241001%3A6; utag_main__ss=0%3Bexp-session; QSI_SI_9AEkoeXmCVAdTMN_intercept=true; __attentive_pv=4; cebsp_=14; urbn_page_visits_count=%7B%22uo-us%22%3A10%7D; _pxhd=Z7VHfFFcdwWKk5LQ12XdE2SYZc/Cd-oGW25/AUNi8y8CJ/K6xUqKwikziahHyukarn29R0CcLabNjkVmhBd8AA==:35cVlkMWUtrCLccY0is-/z60NKlkljpmk0raiTG9HjuuZc9OxeQxYlrmo1Bbn7Ikkls0Of60p/8RMYlku8CXwram2yBi175WzthCStNq1mU=; urbn_auth_payload=%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcyNzkyNjIxNC42MTAwOTM2LCJpYXQiOjE3Mjc5MjU2MTQuNjEwMDkzNiwiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjc4MzczNzkuMDcyMTEwNywgXCJwcm9maWxlSWRcIjogXCI5VHhLcEVkbkl1bkVKTW5kVWh0amN4M2hZc1NUK2xWem8xRVJTa0JzT2p3dnV4TlBrNkpGTTd0NjdrRm94emNyNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09NjEwNDZhY2U0YTM3ZjFiYmVjYWM0YWU2YzA0ZjE5YTRhNDRjODYyNTViNTUxOWZmYmU0NmYyNDZkMjdmMzU4YlwiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIkJBTURURkk1OU1cIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJBUy1TR1wiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiTUhcIn0sIFwiY2FydElkXCI6IFwiYkFIeDExU0JlcVd4d3pXNGJZWlp4Y3F2TndGUE1lSUdSVFA2NkwrM1ZCUlZid1FKb2c0dFUzVGd0ZnVydEhVMTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTUxOGVkOGU0ZjhiZDhjZGI2YzhkZTU2Y2M1YmJiZjk0ZjBhOWY5NzhmYzBhOGUwNDk5ZjY3ZTUxNDM3ZDc4NGJcIn0ifQ.R4aZHjX2bbTRZDeVJgYYFQRT6zwMHx0UaZLG_0sVO4Y%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTc0MzQ3NzYxNC42MTA0NzMsImlhdCI6MTcyNzkyNTYxNC42MTA0NzMsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNzI3OTI1NjE0LjYxMDQ1OSwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJ0cmFjZXJcIjogXCJCQU1EVEZJNTlNXCIsIFwicHJvZmlsZUlkXCI6IFwiOVR4S3BFZG5JdW5FSk1uZFVodGpjeDNoWXNTVCtsVnpvMUVSU2tCc09qd3Z1eE5QazZKRk03dDY3a0ZveHpjcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTYxMDQ2YWNlNGEzN2YxYmJlY2FjNGFlNmMwNGYxOWE0YTQ0Yzg2MjU1YjU1MTlmZmJlNDZmMjQ2ZDI3ZjM1OGJcIn0ifQ.bmmp0xOsA5dZzHR8_bRQ_PR-SlFI8PUGb9dgduCRDHQ%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22BAMDTFI59M%22%2C%22dataCenterId%22%3A%22US-NV%22%2C%22geoRegion%22%3A%22AS-SG%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22MH%22%2C%22country%22%3A%22IN%22%2C%22city%22%3A%22Pune%22%2C%22zipCodes%22%3A%22411002%22%7D%2C%22trueClientIp%22%3A%22106.210.166.22%22%2C%22createdAt%22%3A1727925614614%2C%22authExpiresTime%22%3A1727926094.614%2C%22reauthExpiresTime%22%3A1743477614.614%7D; utag_main__se=19%3Bexp-session; utag_main__st=1727927417326%3Bexp-session; _ga_BBMWPLK0E5=GS1.1.1727923652.3.1.1727925617.60.0.0; _uetsid=fe53f2e0806811ef936c8f99e455d20e; _uetvid=fe55e7c0806811efb1d735c0fdd93126; _tq_id.TV-7209544572-1.e625=9349662df06ba702.1727837393.0.1727925618..; SSRT=cg3-ZgADAA; utag_main_dc_event=9%3Bexp-session; _clsk=dgd4j4%7C1727926275754%7C11%7C0%7Ch.clarity.ms%2Fcollect; _px3=4182ea4b2221ff6617d7ab65776d3b5bf50bd9f51876cb686429155588028f15:CfaBD9QyYimLwJuhMfYNr6PItmFd4+THMKHKCZFvdIy7stlALScu6T4S8Aas24xaEEQvpHCZHiR/sche+coM4A==:1000:DUZpvzsqyH3oGlEPzTmvQWtg9JF9Pss0D+FDOPBfYM+Xx0CFhKVnPtcVOS7QJmBUy/ijbgQq7TdKwpul/YEkbmmE4BI9P1TOkAfatMCZEbvtGRUmwuUE0yRV1nOqJ/hLzisBPu+bXOoYon+KhnfgbfiMjyfxZHP4T2Rq3OLfQ1JfEypctufB3o/pjsieajIhdD4mLlTjpYfd/EhoziHYT+fJF94A1pPw5LnDZs61p80=; _ce.s=v~e10443eeaed793ea24041f08f68306452fe15720~lcw~1727926519073~vir~new~lva~1727837388355~vpv~0~v11.cs~251701~v11.s~dec2e570-8131-11ef-bce2-a9c03c3cf4eb~v11.sla~1727926519829~lcw~1727926519829',
                                             'host': 'www.urbanoutfitters.com',
                                             'referer': 'https://www.urbanoutfitters.com',
                                             'origin': 'https://www.urbanoutfitters.com'},
                                    data=payload).text)
    # print(token)
    return token['authToken']


payload = json.dumps({"pageSize": 72, "skip": 0, "projectionSlug": "categorytiles", "refinements": [
    {"type": "Value", "navigationName": "tile.product.facets.sleeve", "value": "Long Sleeve"}], "personalization": "0",
                      "customerConsent": "true", "featureProductIds": []})

gallery_json = requests.post(
    'https://api.urbanoutfitters.com/api/catalog-search-service/v0/uo-us/tiles/graphic-tees-for-women',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {get_token()}',
        'content-length': '129',
        'authority': 'api.urbanoutfitters.com',
        'origin': 'https://www.urbanoutfitters.com',
        'content-type': 'application/json',
        'priority': 'u=1,i',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'x-urbn-channel': 'web',
        'cookie': 'SSLB=1; urbn_geo_region=AS-SG; urbn_tracer=BAMDTFI59M; urbn_data_center_id=US-NV; _pxvid=f78f8421-8068-11ef-9605-4d9dbd186e73; __pxvid=fa9e6192-8068-11ef-a45f-0242ac120003; _ga=GA1.1.178813237.1727837389; utag_main_v_id=01924b22455a000235b07ff6d5cc0507d0020075007e8; _gcl_au=1.1.1539530721.1727837391; smartDash=8e3012a1-84a7-49ef-98d0-77d9aa9b369c; _scid=b-0F8vRovPhmY38sX9lmdnLywXxMyFDA; _pin_unauth=dWlkPVl6TXlPRFpoWXpFdE1XVTVNQzAwWXpKaExXRmlOV1V0TTJZMFlqazVORFl5TVRrdw; _fbp=fb.1.1727837394581.212925117775355125; _tt_enable_cookie=1; _ttp=L2-3ukyGvcQCAiotwjY0FEcHdjb; smartDashLRX=000; __adroll_fpc=71e8e77344487dcb3d0a7a07eb5e75dc-1727837396847; _lc2_fpi=18c6eee2a756--01j95j4rr5j2ayenjxzvxgnqb2; BVBRANDID=f696e4e8-652f-442f-b6e5-94ecc11b6b0c; _svsid=d0001b28c830d40e3f8f58420cd1f964; ss-enable-bisn-confirmation=1; SSSC=472.G7421005031593265002.15|85305.2689651:85552.2694268:85998.2705798:86053.2707306; pxcts=8aa62a37-922d-11ef-b23b-b550812c7c9c; utag_main__sn=15; utag_main_ses_id=1729790978920%3Bexp-session; utag_main_isLoggedIn=false%3Bexp-session; utag_main__ss=0%3Bexp-session; _clck=2ammpq%7C2%7Cfqa%7C0%7C1736; cebs=1; _ce.clock_data=352%2C103.185.235.101%2C1%2C9fae7894890fe21cd77090af114aa2cd%2CEdge%2CIN; _li_dcdm_c=.urbanoutfitters.com; utag_main_dc_visit=15; utag_main_dc_region=ap-east-1%3Bexp-session; ranMID=43176; _ScCbts=%5B%5D; BVBRANDSID=c58f77f5-216a-402b-86ba-591c28f2c237; SSID=CQCbmx04ABAAAADCtPxmaseAEMK0_GYPAAAAAAApIfVo_YMaZwAU-SVQAQNqTykA_YMaZwEA7k8BA4ZJKQD9gxpnAQAwTgEBfBwpAP2DGmcBADlNAQFzCikA_YMaZwEAs0MBALxMAQAWSwEAt04BAA; SSRT=cpQaZwADAA; rmStore=ald:20241024_1839|atrv:svunC25memk-qelmPD3RtsoWlwXRquYjyg; _rdt_uuid=1727837392751.5e599515-0526-407a-b9a7-a9379cbffd05; utag_main_dc_event=34%3Bexp-session; _uetsid=8d007a90922d11ef97f3bf48e52233de; _uetvid=fe55e7c0806811efb1d735c0fdd93126; _scid_r=dW0F8vRovPhmY38sX9lmdnLywXxMyFDAGsFz_g; cebsp_=28; _ce.s=v~e10443eeaed793ea24041f08f68306452fe15720~lcw~1729795228250~vir~returning~lva~1729790980305~vpv~4~v11slnt~1728588709551~v11.cs~251701~v11.s~f9d0cc60-9234-11ef-bd2f-375de10f257e~v11.sla~1729795229251~v11.send~1729795228250~lcw~1729795229251; utag_main__pn=16%3Bexp-session; _pxhd=T10DW5XgL8jnlSF5MAkc991gejHFzfvA7etoAGVOb6DdJe5RwvMOPvnl6AjjVuXuxeMjC189OSladwF3Z1VbRw==:jT12epRI-9GW/4Qt9aNG4ljR0-6T9Z-PB9uqjpOY4uVxlXqVHGHivx831sjro00mnGdsCs9xwFORstQkIJE3rTbekDvUmIjCyzqWXhL9GpE=; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+25+2024+00%3A10%3A34+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=4ca70fba-632a-4f41-8bfb-a3d4fa011b70&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.urbanoutfitters.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _clsk=1bu17mj%7C1729795239340%7C40%7C1%7Ct.clarity.ms%2Fcollect; _px3=4cb96563f64773f14d82a1084c27365bfdc3ab57e0ea53e2963c2d83d698d117:U2Mmg7SbmxlYNOnERUWHthNcE1BfUoRMJUXb0Y5OaQy1dcw9x4IMN/s9XudE2sSXE5o0CxJJ81Zx/KQW5CAf8g==:1000:yiAfpGtgWe3l5perx1RjzOoUXTfEhrGNq7Spe2QPl1Vkv4q6zndk284vwFU2+hHkV7T7B4aS8KUxwt9xXQIWkO0xshDy1rjkFTvyyyzOQ+Vdilm6cXt1Gi4niqZBmGqiAI01VcWZ9pJsuM/0k7TkznVjek+fnrJnQ7XnFEl+dlAqYJbhgsK/6wrSCNfrNzD/t9U4p9k/gaIVFVI+f8C7KOAE7QrZBh/TCeDGDIO6ouU=; urbn_auth_payload=%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcyOTc5NjExOS42MzQzNjYzLCJpYXQiOjE3Mjk3OTU1MTkuNjM0MzY2MywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjc4MzczNzkuMDcyMTEwNywgXCJwcm9maWxlSWRcIjogXCI5VHhLcEVkbkl1bkVKTW5kVWh0amN4M2hZc1NUK2xWem8xRVJTa0JzT2p3dnV4TlBrNkpGTTd0NjdrRm94emNyNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09NjEwNDZhY2U0YTM3ZjFiYmVjYWM0YWU2YzA0ZjE5YTRhNDRjODYyNTViNTUxOWZmYmU0NmYyNDZkMjdmMzU4YlwiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIkJBTURURkk1OU1cIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJBUy1TR1wiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiTUhcIn0sIFwiY2FydElkXCI6IFwiYkFIeDExU0JlcVd4d3pXNGJZWlp4Y3F2TndGUE1lSUdSVFA2NkwrM1ZCUlZid1FKb2c0dFUzVGd0ZnVydEhVMTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTUxOGVkOGU0ZjhiZDhjZGI2YzhkZTU2Y2M1YmJiZjk0ZjBhOWY5NzhmYzBhOGUwNDk5ZjY3ZTUxNDM3ZDc4NGJcIn0ifQ.oW0kOI2-ZiAhByYqTR8g6YE621tesKbPfy5FgypGVTA%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTc0NTM0NzUxOS42MzQ3NDk0LCJpYXQiOjE3Mjk3OTU1MTkuNjM0NzQ5NCwiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjk3OTU1MTkuNjM0NzM1OCwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJ0cmFjZXJcIjogXCJCQU1EVEZJNTlNXCIsIFwicHJvZmlsZUlkXCI6IFwiOVR4S3BFZG5JdW5FSk1uZFVodGpjeDNoWXNTVCtsVnpvMUVSU2tCc09qd3Z1eE5QazZKRk03dDY3a0ZveHpjcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTYxMDQ2YWNlNGEzN2YxYmJlY2FjNGFlNmMwNGYxOWE0YTQ0Yzg2MjU1YjU1MTlmZmJlNDZmMjQ2ZDI3ZjM1OGJcIn0ifQ.epyp240oUP2lwTwi89TkqxYBnENQdfghCKg_eNiOPe0%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22BAMDTFI59M%22%2C%22dataCenterId%22%3A%22US-NV%22%2C%22geoRegion%22%3A%22AS-SG%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22MH%22%2C%22country%22%3A%22IN%22%2C%22city%22%3A%22Pune%22%2C%22zipCodes%22%3A%22411001%22%7D%2C%22trueClientIp%22%3A%22106.220.159.143%22%2C%22createdAt%22%3A1729795519638%2C%22authExpiresTime%22%3A1729795999.638%2C%22reauthExpiresTime%22%3A1745347519.638%7D; utag_main__se=87%3Bexp-session; utag_main__st=1729797323029%3Bexp-session; _ga_BBMWPLK0E5=GS1.1.1729790980.16.1.1729795523.60.0.0',
        'x-urbn-country': 'IN',
        'x-urbn-currency': 'USD',
        'x-urbn-experience': 'ss',
        'x-urbn-geo-region': 'US-NV',
        'x-urbn-language': 'en-US',
        'x-urbn-pool': 'INTL_DIRECT',
        'x-urbn-primary-data-center-id': 'US-NV',
        'x-urbn-site-id': 'uo-us'
    },
    data=payload)
print(gallery_json.text)

# exit()

# payload = json.dumps({
#     "reauthToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTc0MzQ3NzYxNC42MTA0NzMsImlhdCI6MTcyNzkyNTYxNC42MTA0NzMsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNzI3OTI1NjE0LjYxMDQ1OSwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJ0cmFjZXJcIjogXCJCQU1EVEZJNTlNXCIsIFwicHJvZmlsZUlkXCI6IFwiOVR4S3BFZG5JdW5FSk1uZFVodGpjeDNoWXNTVCtsVnpvMUVSU2tCc09qd3Z1eE5QazZKRk03dDY3a0ZveHpjcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTYxMDQ2YWNlNGEzN2YxYmJlY2FjNGFlNmMwNGYxOWE0YTQ0Yzg2MjU1YjU1MTlmZmJlNDZmMjQ2ZDI3ZjM1OGJcIn0ifQ.bmmp0xOsA5dZzHR8_bRQ_PR-SlFI8PUGb9dgduCRDHQ"})
# res = requests.put('https://www.urbanoutfitters.com/slipstream/api/token/v0/uo-us/auth',
#                    headers={'accept': 'application/json, text/plain, */*',
#                             'accept-encoding': 'gzip, deflate, br, zstd',
#                             'accept-language': 'en-US,en;q=0.9',
#                             'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcyNzkyNjIxNC42MTAwOTM2LCJpYXQiOjE3Mjc5MjU2MTQuNjEwMDkzNiwiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjc4MzczNzkuMDcyMTEwNywgXCJwcm9maWxlSWRcIjogXCI5VHhLcEVkbkl1bkVKTW5kVWh0amN4M2hZc1NUK2xWem8xRVJTa0JzT2p3dnV4TlBrNkpGTTd0NjdrRm94emNyNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09NjEwNDZhY2U0YTM3ZjFiYmVjYWM0YWU2YzA0ZjE5YTRhNDRjODYyNTViNTUxOWZmYmU0NmYyNDZkMjdmMzU4YlwiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIkJBTURURkk1OU1cIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJBUy1TR1wiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiTUhcIn0sIFwiY2FydElkXCI6IFwiYkFIeDExU0JlcVd4d3pXNGJZWlp4Y3F2TndGUE1lSUdSVFA2NkwrM1ZCUlZid1FKb2c0dFUzVGd0ZnVydEhVMTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTUxOGVkOGU0ZjhiZDhjZGI2YzhkZTU2Y2M1YmJiZjk0ZjBhOWY5NzhmYzBhOGUwNDk5ZjY3ZTUxNDM3ZDc4NGJcIn0ifQ.R4aZHjX2bbTRZDeVJgYYFQRT6zwMHx0UaZLG_0sVO4Y',
#                             'connection': 'keep-alive',
#                             'content-length': '541',
#                             'content-type': 'application/json',
#                             'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#                             'sec-ch-ua-mobile': '?0',
#                             'sec-ch-ua-platform': "Windows",
#                             'sec-fetch-dest': 'empty',
#                             'sec-fetch-mode': 'cors',
#                             'sec-fetch-site': 'same-origin',
#                             'x-urbn-channel': 'web',
#                             'x-urbn-country': 'IN',
#                             'x-urbn-currency': 'USD',
#                             'x-urbn-experience': 'ss',
#                             'x-urbn-geo-region': 'AS-SG',
#                             'x-urbn-language': 'en-US',
#                             'x-urbn-primary-data-center-id': 'US-NV',
#                             'x-urbn-site-id': 'uo-us',
#                             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
#                             'cookie': 'SSLB=1; urbn_site_id=uo-us; urbn_edgescape_site_id=uo-us; urbn_language=en-US; urbn_uuid=4ca70fba-632a-4f41-8bfb-a3d4fa011b70; urbn_channel=web; urbn_geo_region=AS-SG; siteId=uo-us; urbn_inventory_pool=INTL_DIRECT; urbn_tracer=BAMDTFI59M; urbn_currency=USD; urbn_country=IN; urbn_data_center_id=US-NV; urbn_device_info=web%7Cother%7Cdesktop; pxcts=f9713cae-8068-11ef-b763-c795d5131f7a; _pxvid=f78f8421-8068-11ef-9605-4d9dbd186e73; __pxvid=fa9e6192-8068-11ef-a45f-0242ac120003; cebs=1; _ga=GA1.1.178813237.1727837389; utag_main_v_id=01924b22455a000235b07ff6d5cc0507d0020075007e8; _gcl_au=1.1.1539530721.1727837391; __attentive_id=14f399d136e147168b6acc0444566215; _attn_=eyJ1Ijoie1wiY29cIjoxNzI3ODM3MzkyNTUyLFwidW9cIjoxNzI3ODM3MzkyNTUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjE0ZjM5OWQxMzZlMTQ3MTY4YjZhY2MwNDQ0NTY2MjE1XCJ9In0=; __attentive_cco=1727837392557; smartDash=8e3012a1-84a7-49ef-98d0-77d9aa9b369c; _scid=b-0F8vRovPhmY38sX9lmdnLywXxMyFDA; _pin_unauth=dWlkPVl6TXlPRFpoWXpFdE1XVTVNQzAwWXpKaExXRmlOV1V0TTJZMFlqazVORFl5TVRrdw; _fbp=fb.1.1727837394581.212925117775355125; _tt_enable_cookie=1; _ttp=L2-3ukyGvcQCAiotwjY0FEcHdjb; smartDashLRX=000; __adroll_fpc=71e8e77344487dcb3d0a7a07eb5e75dc-1727837396847; _li_dcdm_c=.urbanoutfitters.com; _lc2_fpi=18c6eee2a756--01j95j4rr5j2ayenjxzvxgnqb2; _ScCbts=%5B%5D; BVBRANDID=f696e4e8-652f-442f-b6e5-94ecc11b6b0c; ss-enable-bisn-confirmation=1; SS_SHOP_THE_LOOK_VARIANT=0; SSID=CQB48x0qAAQAAADCtPxmaseAEMK0_GYDAAAAAACDkyVnVwX-ZgAU-TlNAQFzCikAVwX-ZgEAvEwBA3n-KADCtPxmAwAWSwEDC90oAFcF_mYBALNDAQA; SSSC=472.G7421005031593265002.3|84758.2678027:85180.2686585:85305.2689651; urbn_uuid_session=eaa440f6-0b76-4ce8-a66f-22dc5b98559c; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Oct+03+2024+08%3A16%3A25+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=4ca70fba-632a-4f41-8bfb-a3d4fa011b70&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.urbanoutfitters.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; utag_main__sn=3; utag_main_ses_id=1727923587061%3Bexp-session; utag_main__pn=1%3Bexp-session; utag_main_isLoggedIn=false%3Bexp-session; utag_main_dc_visit=3; utag_main_dc_region=ap-east-1%3Bexp-session; _clck=2ammpq%7C2%7Cfpp%7C0%7C1736; _rdt_uuid=1727837392751.5e599515-0526-407a-b9a7-a9379cbffd05; _scid_r=bG0F8vRovPhmY38sX9lmdnLywXxMyFDAGsFzuQ; __ar_v4=TLGS2MDMOFEALNQLHLTLBW%3A20241001%3A6%7CQWC5THA5TZFOLOWWLOOPBD%3A20241001%3A6; utag_main__ss=0%3Bexp-session; QSI_SI_9AEkoeXmCVAdTMN_intercept=true; __attentive_pv=4; cebsp_=14; urbn_page_visits_count=%7B%22uo-us%22%3A10%7D; _pxhd=Z7VHfFFcdwWKk5LQ12XdE2SYZc/Cd-oGW25/AUNi8y8CJ/K6xUqKwikziahHyukarn29R0CcLabNjkVmhBd8AA==:35cVlkMWUtrCLccY0is-/z60NKlkljpmk0raiTG9HjuuZc9OxeQxYlrmo1Bbn7Ikkls0Of60p/8RMYlku8CXwram2yBi175WzthCStNq1mU=; urbn_auth_payload=%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcyNzkyNjIxNC42MTAwOTM2LCJpYXQiOjE3Mjc5MjU2MTQuNjEwMDkzNiwiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3Mjc4MzczNzkuMDcyMTEwNywgXCJwcm9maWxlSWRcIjogXCI5VHhLcEVkbkl1bkVKTW5kVWh0amN4M2hZc1NUK2xWem8xRVJTa0JzT2p3dnV4TlBrNkpGTTd0NjdrRm94emNyNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09NjEwNDZhY2U0YTM3ZjFiYmVjYWM0YWU2YzA0ZjE5YTRhNDRjODYyNTViNTUxOWZmYmU0NmYyNDZkMjdmMzU4YlwiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIkJBTURURkk1OU1cIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJBUy1TR1wiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiTUhcIn0sIFwiY2FydElkXCI6IFwiYkFIeDExU0JlcVd4d3pXNGJZWlp4Y3F2TndGUE1lSUdSVFA2NkwrM1ZCUlZid1FKb2c0dFUzVGd0ZnVydEhVMTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTUxOGVkOGU0ZjhiZDhjZGI2YzhkZTU2Y2M1YmJiZjk0ZjBhOWY5NzhmYzBhOGUwNDk5ZjY3ZTUxNDM3ZDc4NGJcIn0ifQ.R4aZHjX2bbTRZDeVJgYYFQRT6zwMHx0UaZLG_0sVO4Y%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTc0MzQ3NzYxNC42MTA0NzMsImlhdCI6MTcyNzkyNTYxNC42MTA0NzMsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNzI3OTI1NjE0LjYxMDQ1OSwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJ0cmFjZXJcIjogXCJCQU1EVEZJNTlNXCIsIFwicHJvZmlsZUlkXCI6IFwiOVR4S3BFZG5JdW5FSk1uZFVodGpjeDNoWXNTVCtsVnpvMUVSU2tCc09qd3Z1eE5QazZKRk03dDY3a0ZveHpjcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTYxMDQ2YWNlNGEzN2YxYmJlY2FjNGFlNmMwNGYxOWE0YTQ0Yzg2MjU1YjU1MTlmZmJlNDZmMjQ2ZDI3ZjM1OGJcIn0ifQ.bmmp0xOsA5dZzHR8_bRQ_PR-SlFI8PUGb9dgduCRDHQ%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22BAMDTFI59M%22%2C%22dataCenterId%22%3A%22US-NV%22%2C%22geoRegion%22%3A%22AS-SG%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22MH%22%2C%22country%22%3A%22IN%22%2C%22city%22%3A%22Pune%22%2C%22zipCodes%22%3A%22411002%22%7D%2C%22trueClientIp%22%3A%22106.210.166.22%22%2C%22createdAt%22%3A1727925614614%2C%22authExpiresTime%22%3A1727926094.614%2C%22reauthExpiresTime%22%3A1743477614.614%7D; utag_main__se=19%3Bexp-session; utag_main__st=1727927417326%3Bexp-session; _ga_BBMWPLK0E5=GS1.1.1727923652.3.1.1727925617.60.0.0; _uetsid=fe53f2e0806811ef936c8f99e455d20e; _uetvid=fe55e7c0806811efb1d735c0fdd93126; _tq_id.TV-7209544572-1.e625=9349662df06ba702.1727837393.0.1727925618..; SSRT=cg3-ZgADAA; utag_main_dc_event=9%3Bexp-session; _clsk=dgd4j4%7C1727926275754%7C11%7C0%7Ch.clarity.ms%2Fcollect; _px3=4182ea4b2221ff6617d7ab65776d3b5bf50bd9f51876cb686429155588028f15:CfaBD9QyYimLwJuhMfYNr6PItmFd4+THMKHKCZFvdIy7stlALScu6T4S8Aas24xaEEQvpHCZHiR/sche+coM4A==:1000:DUZpvzsqyH3oGlEPzTmvQWtg9JF9Pss0D+FDOPBfYM+Xx0CFhKVnPtcVOS7QJmBUy/ijbgQq7TdKwpul/YEkbmmE4BI9P1TOkAfatMCZEbvtGRUmwuUE0yRV1nOqJ/hLzisBPu+bXOoYon+KhnfgbfiMjyfxZHP4T2Rq3OLfQ1JfEypctufB3o/pjsieajIhdD4mLlTjpYfd/EhoziHYT+fJF94A1pPw5LnDZs61p80=; _ce.s=v~e10443eeaed793ea24041f08f68306452fe15720~lcw~1727926519073~vir~new~lva~1727837388355~vpv~0~v11.cs~251701~v11.s~dec2e570-8131-11ef-bce2-a9c03c3cf4eb~v11.sla~1727926519829~lcw~1727926519829',
#                             'host': 'www.urbanoutfitters.com',
#                             'referer':'https://www.urbanoutfitters.com/dresses?page=3&sleeve=Sleeveless',
#                             'origin': 'https://www.urbanoutfitters.com'},
#                    data=payload)
#
# payload = json.dumps({"pageSize": 72, "skip": 72, "projectionSlug": "categorytiles", "refinements": [
#     {"type": "Value", "navigationName": "tile.product.facets.sleeve", "value": "Sleeveless"}], "personalization": "0",
#                       "customerConsent": "true", "featureProductIds": []})

# res = requests.post('https://api.urbanoutfitters.com/api/catalog-search-service/v0/uo-us/tiles/womens-tops',
#                     headers={
#                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
#                         'scheme': 'https',
#                         'accept': 'application/json, text/plain, */*',
#                         'accept-encoding': 'gzip, deflate, br, zstd',
#                         'accept-language': 'en-US,en;q=0.9',
#                         'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcyNzkyNzEyMC4zMjI4NTUsImlhdCI6MTcyNzkyNjUyMC4zMjI4NTUsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNzI3ODM3Mzc5LjA3MjExMDcsIFwicHJvZmlsZUlkXCI6IFwiOVR4S3BFZG5JdW5FSk1uZFVodGpjeDNoWXNTVCtsVnpvMUVSU2tCc09qd3Z1eE5QazZKRk03dDY3a0ZveHpjcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTYxMDQ2YWNlNGEzN2YxYmJlY2FjNGFlNmMwNGYxOWE0YTQ0Yzg2MjU1YjU1MTlmZmJlNDZmMjQ2ZDI3ZjM1OGJcIiwgXCJhbm9ueW1vdXNcIjogdHJ1ZSwgXCJ0cmFjZXJcIjogXCJCQU1EVEZJNTlNXCIsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwic2l0ZUlkXCI6IFwidW8tdXNcIiwgXCJicmFuZElkXCI6IFwidW9cIiwgXCJzaXRlR3JvdXBcIjogXCJ1by11c1wiLCBcImRhdGFDZW50ZXJJZFwiOiBcIlVTLU5WXCIsIFwiZ2VvUmVnaW9uXCI6IFwiQVMtU0dcIiwgXCJlZGdlc2NhcGVcIjoge1wicmVnaW9uQ29kZVwiOiBcIk1IXCJ9LCBcImNhcnRJZFwiOiBcImJBSHgxMVNCZXFXeHd6VzRiWVpaeGNxdk53RlBNZUlHUlRQNjZMKzNWQlJWYndRSm9nNHRVM1RndGZ1cnRIVTE1VSszcnMycnhoam00cEQzMENjSUJ3PT01MThlZDhlNGY4YmQ4Y2RiNmM4ZGU1NmNjNWJiYmY5NGYwYTlmOTc4ZmMwYThlMDQ5OWY2N2U1MTQzN2Q3ODRiXCJ9In0.WOaZBG3UUi5D-ZrHAYL9JsQ9MH5mIzrwoLcgA4yLmbE',
#                         'content-length': '228',
#                         'content-type': 'application/json',
#                         'priority': 'u = 1, i',
#                         'sec-ch-ua': '"Microsoft Edge";v = "129", "Not=A?Brand";v = "8", "Chromium";v = "129"',
#                         'sec-ch-ua-mobile': '?0',
#                         'sec-ch-ua-platform': 'Windows',
#                         'sec-fetch-dest': 'empty',
#                         'sec-fetch-mode': 'cors',
#                         'sec-fetch-site': 'same-site',
#                         'x-urbn-channel': 'web',
#                         'x-urbn-country': 'IN',
#                         'x-urbn-currency': 'USD',
#                         'x-urbn-experience': 'ss',
#                         'x-urbn-geo-region': 'AS-SG',
#                         'x-urbn-language': 'en-US',
#                         'x-urbn-pool': 'INTL_DIRECT',
#                         'x-urbn-primary-data-center-id': 'US-NV',
#                         'x-urbn-site-id': 'uo-us'
#                     },
#                     data=payload)
#
# # print(res.text)
api_res = json.loads(gallery_json.text)
# print(api_res)
# exit()
final_df = pd.DataFrame(
    columns=['Product_Category', 'Category', 'Subcategory1', 'Subcategory2', 'Subcategory3', 'Url', 'Attr_Name',
             'Attr_Value'])
ctr = 0
valid_attr_list = ['Occasion', 'Color', 'Length', 'Sleeve', 'Style', 'Neckline', 'Material']

for attr in api_res['availableNavigation']:
    if attr['displayName'] in valid_attr_list:
        print(attr['displayName'])
        for attr_value in attr['refinements']:
            final_df.at[ctr, 'Product_Category'] = 'Clothing'
            final_df.at[ctr, 'Category'] = 'Women'
            final_df.at[ctr, 'Subcategory1'] = 'Western'
            final_df.at[ctr, 'Subcategory2'] = 'Topwear'
            final_df.at[ctr, 'Subcategory3'] = 'T-Shirts'
            final_df.at[
                ctr, 'Url'] = f'https://www.urbanoutfitters.com/graphic-tees-for-women?page=3&{attr["displayName"]}={attr_value["value"]}'
            final_df.at[ctr, 'Refinement'] = attr['name']
            final_df.at[ctr, 'Ref_Value'] = attr_value['value']
            final_df.at[ctr, 'Attr_Name'] = attr['displayName']

            final_df.at[ctr, 'Attr_Value'] = attr_value['value'].title()
            ctr += 1
#
final_df.to_csv('Urbanoutfitters_tees_with_attrs.csv', index=False, index_label=False)
