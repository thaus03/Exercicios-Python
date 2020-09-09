from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient('mongodb://igor:Admin123@m-atlas-shard-00-00-htfhe.azure.mongodb.net:27017,m-atlas-shard-00-01-htfhe.azure.mongodb.net:27017,m-atlas-shard-00-02-htfhe.azure.mongodb.net:27017/test?ssl=true&replicaSet=M-Atlas-shard-0&authSource=admin&retryWrites=true&w=majority')

db = client['TestDB']       # or db = client.TestDB
dados = db.cadastro         # Defino a collection que eu quero

# Para printar o primeiro, não é necessário abrir um cursor
print(dados.find_one())

# Abro o Cursor para fazer a busca de dados
cursor = dados.find({}, {"nome": 1, "_id": 0})

# print(dumps(cursor, indent=2))    //pretty
#print(dumps(cursor))
