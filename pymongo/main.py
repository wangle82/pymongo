
print("hello python");
from pymongo import MongoClient
from elasticsearch import Elasticsearch
mc =MongoClient("yl-mongodb-mams-online001-bjdxt.qiyi.virtual",27017);
db = mc.search
# mc.a
c =db.author.find()
# db.author.insert({"name":'zhj',"age":24})
# for o in c:
#     print(o)
one = db.author.find({"name": 'zhj'})
print(one)
# db.author.remove({"name":"test2"});
# db.author.insert({"name":"test2"});
# c =db.author.find()
# #
# for o in c:
#      print(o)
# test="10.15.226.153"
# online = "10.15.212.31";
# es = Elasticsearch(hosts=online)
#
# search = es.search(index='chapter', q='id:115962804')
#
# print(search)
