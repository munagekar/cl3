from pymongo import MongoClient
# Usually this should work fine if on same machine
client = MongoClient()

# Incase Mongo user and password to be used
#client=MongoClient('mongodb://admin:admin123@ip:port')

# Mongo->DB->Col->Document


db = client.dbname

doc0= {"phil":"0","food":"rice"}
doc1= {"phil":"1","food":"noodles"}
doc2= {"phil":"2","food":"sushi"}
doc3= {"phil":"3","food":"dosa"}
doc4= {"phil":"4","food":"wada"}

docs = [doc0,doc1,doc2,doc3,doc4]

db.colname.insert_many(docs)




