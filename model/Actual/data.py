import codecs
import csv
import pymongo
import pandas as pd 
# 链接mongo数据库
mongo_client = pymongo.MongoClient('mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/test?authSource=admin&replicaSet=atlas-vtcq3b-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db = mongo_client.Survey
my_collection = db['survey'] 


list_tmp = []
for r in my_collection.find():
    list_tmp.append(r)
data = pd.DataFrame(list_tmp)
print(list_tmp)
print(data)

# #查询库中数据
# cursor = my_collection.find()
# print(cursor)
# #打开csv文件

# with codecs.open('data1.csv', 'w', 'utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     # 先写入columns_name
#     writer.writerow(["_id","name","email","department","employee_details","employee_risk_level"])
#     #写入多行用writerows
#     for data in cursor:
#         writer.writerows([[data["_id"], data["name"],data["email"],data["department"],data["employee_details"],data["employee_risk_level"] ]])


#         # data["topic"], data["1"],data["2"],data["7"],data["8"],data["9"],data["10"],data["11"]
#         # "name", "content", "topic", "at","1","2","7","8","9","10","11"