from pymongo import MongoClient

client = MongoClient('mongodb://igor:Admin123@m-atlas-shard-00-00-htfhe.azure.mongodb.net:27017,m-atlas-shard-00-01-htfhe.azure.mongodb.net:27017,m-atlas-shard-00-02-htfhe.azure.mongodb.net:27017/test?ssl=true&replicaSet=M-Atlas-shard-0&authSource=admin&retryWrites=true&w=majority')

#client = MongoClient("mongodb+srv://igor:Admin123@m-atlas-htfhe.azure.mongodb.net/TesteDB?retryWrites=true&w=majority")

db = client['TestDB']
survey = db.survey
cadastro = db.cadastro
#client.list_collection_names()

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
cidade = str(input('Digite sua cidade: '))

result = cadastro.insert_one({"nome": nome,
                              "idade": idade,
                              "cidade": cidade})

print("Dados cadastrados no Banco de dados")
print("Seu nome é {}, você tem {} anos e mora em {}".format(result.nome, result.idade, result.cidade))
#print(survey.find_one())




