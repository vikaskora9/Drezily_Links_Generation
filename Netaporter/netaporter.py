import requests

resp = requests.get(
    'https://www.net-a-porter.com/api/nap/search/resources/store/nap_us/productview/byCategory?attrs=true&category=%2Fclothing%2Fdenim&locale=en_US&pageNumber=2&pageSize=60',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'authority': 'www.net-a-porter.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'application-name': 'Blue lobster',
        'application-version': '4.835.0',
        'x-ibm-client-id': '95f14cbd-793e-46ec-9f76-6fac2fbb6683'
    })

print(resp.text)
