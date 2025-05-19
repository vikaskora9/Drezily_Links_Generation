import requests
from bs4 import BeautifulSoup

# productDetailsModal__modal-body
resp = BeautifulSoup(requests.get(
    'https://usa.tommy.com/en/women/clothing/dresses/ruffle-collar-pleated-georgette-dress/WW44556-09Z.html',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        }).text, 'html.parser')
# print(resp.text)
try:
    print(resp.find('div', {'product-image'}).find('img')['src'])
except:
    print(resp.text)
