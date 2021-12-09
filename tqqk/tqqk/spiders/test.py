import pymongo
import pandas as pd

client=pymongo.MongoClient('localhost',27017)
db=client['天气']
table=db['scrapy_items1']
data=pd.DataFrame(list(table.find({'地区':'60103'})))
print(data.head(5))
print(len(data))
