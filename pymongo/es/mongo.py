
from pymongo import MongoClient
mc =MongoClient("yl-mongodb-mams-online001-bjdxt.qiyi.virtual",27017);
db = mc.search

#查一个collection(author)
c =db.author.find()
# c = db.author.count();
print(c)
#遍历一个集合
for doc in c:
    print(doc);

# # 查一个doc
# dc=db.author.find_one({"name":"zhj"})
# print(dc)
#
# # 删除记录
# db.author.remove({"name":"test"});
#
# #增加一个document
# db.author.insert({"name":"zhj","age":10});
# dc=db.author.find_one({"name":"wl"});
# print(dc)
#
# #修改记录(文档替换)
# db.author.update({"name":"test"},{"$set":{"Email":"libing@126.com","Password":"123"}})
#
# # 部分修改(原来有这个字段)
# db.author.update({"name":"zhj"},{"$set":{"age":6}})
