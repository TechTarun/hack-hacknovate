from pymongo import MongoClient
client = MongoClient("mongodb://tarun:tarun@hacknovate-shard-00-00-stlyh.mongodb.net:27017,hacknovate-shard-00-01-stlyh.mongodb.net:27017,hacknovate-shard-00-02-stlyh.mongodb.net:27017/test?ssl=true&replicaSet=Hacknovate-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database("site_data")
records = db.sample
"""record_num = records.count_documents({})
print(record_num)

new_record = {"name":"vaibhav", "number":9871846168}
records.insert_one(new_record)"""
record_list = list(records.find())
for record in record_list:
    if(int(record['number']) == 919759644218):
        print(record['name'])
        
