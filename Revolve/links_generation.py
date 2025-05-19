import json
import math
import pymongo
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('/Users/shardakora/Desktop/Data/Revolve/prod_links.csv')

upd = []

for i, row in df.iterrows():
    try:
        upd.append(pymongo.UpdateOne({'Source': 'Revolve','Item_Url': row['Item_Url']},
                                    {
                                        '$set':{
                                            'Selling_Price':float(row['Selling_Price'].replace(',', '')),
                                            'Original_Price':float(row['Original_Price'].replace(',', '')),
                                            'Discount_Percentage': math.floor((1 - (float(row['Selling_Price'].replace(',', '')) / float(row['Original_Price'].replace(',', '')))) * 100)
                                        }
                                    }))
    except:
        pass

print(upd)

db = pymongo.MongoClient('mongodb://redFyndProD:Ar3visdotAIrEdFynD@18.144.12.199:27017/')['DrezilyItemMasterDB']['item_master']

res = db.bulk_write(upd, ordered=False)
print(res.matched_count, res.modified_count)