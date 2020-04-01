Exercicio MONGODB

## Exercicio 1

Resposta de cada questao seguir a sequencia de comandos

### `db.pets.insert([{"name": "Bilbo", "species": "Peixe"}, {"name": "Frodo", "species": "Hamster"}])`
### `db.pets.count()`
### `db.pets.findOne()`
### `db.pets.find({species: "Gato", name: "Kilha"})`
### `db.pets.find({_id : ObjectId('5e847e22e936d2fd10843bd0')})`
### `db.pets.find({species: "Hamster"})`
### `db.pets.find({name: "Mike"})`
### `db.pets.find({species: "Cachorro", name: "Mike"})`

## Exercicio 2

Resposta de cada questao seguir a sequencia de comandos

### `db.italians.find({age : {$eq: 99}}).count()`
### `db.italians.find({age : {$gt: 65}}).count()`
### `db.italians.find({age : {$gt: 12}, age : {$lt: 18}}).count()`
### `db.italians.find({cat : {$exists: true}})`
### `db.italians.find({dog : {$exists: true}})`
### `db.italians.find({cat : {$exists: false}, dog : {$exists: false}})`
### `db.italians.find({cat : {$exists: true}, age : {$gt: 65}}).count()`
### `db.italians.find({age : {$gt: 12}, age : {$lt: 18}, dog : {$exists: true}}).count()`
### `db.italians.find( { $where: function() {    return ("cat".length > 0 && "dog".length > 0) } } ).pretty()`
### `db.italians.find({ '$expr': { '$lt': [ "$age" , "$cat.age" ] } }).pretty()`
### `db.italians.find({ '$expr': { '$eq': [ "$firstname" , "$cat.name" ] } }).pretty()`
### `db.italians.find({bloodType: /-/ }, {"firstname" : 1, "surname" : 1})`
### `db.italians.find({}, {"cat" : 1, "dog" : 1})`
### `db.italians.find({surname: "Rossi"}).sort({age: -1}).limit(5)`
### `db.italians.insert({'firstname': 'Monica', 'surname': 'Rossi', 'username': 'user9866', 'age': 78.0, 'email': 'Monica.Rossi@live.com', 'bloodType': 'O-', 'id_num': '424547604835', 'registerDate': '2020-04-1', 'ticketNumber': 6907.0, 'jobs': ['Logística', 'Engenharia Têxtil'], 'favFruits': ['Goiaba', 'Maçã', 'Maçã'], 'movies': [{'title': 'Um Estranho no Ninho (1975)', 'rating': 3.27}, {'title': 'O Senhor dos Anéis: A Sociedade do Anel (2001)', 'rating': 2.01}, {'title': 'A Felicidade Não se Compra (1946)', 'rating': 4.27}, {'title': 'Seven: Os Sete Crimes Capitais (1995)', 'rating': 2.45}, {'title': 'Forrest Gump: O Contador de Histórias (1994)', 'rating': 2.34}], 'mother': {'firstname': 'Gianni', 'surname': 'Rossi', 'age': 104.0}, 'cat': {'name': 'Enzo', 'age': 1.0}, 'lion': {'name': 'Fofinho', 'age': 5.0}})`
### `db.italians.deleteOne({'lion': { '$exists': 'true'}})`
### `db.italians.updateMany({}, {$inc : {age : 1, "cat.age" : 1, "dog.age": 1}})`
### `db.italians.deleteMany({'cat': { '$exists': 'true'}, age : 66})`
### `db.italians.aggregate([{'$match': {'$expr': {'$eq': ["$firstname", "$mother.firstname"]}}}, {'$match': {'$or':[{'cat': {'$exists': 'true'}}, {'dog': {'$exists': 'true'}}]}}])`
### `db.italians.aggregate([ { '$project' : { 'firstname' : 1, '_id': 0 } } ])`
### `db.italians.aggregate([ { '$project' : { 'firstname' : 1, 'surname': 1, '_id': 0 } } ])`
### `db.italians.find({'favFruits': { '$all': ["Banana", "Maçã"] }, '$or': [{'cat': {'$exists': 'true'}}, {'dog': {'$exists': 'true'}}], '$and': [{'age': {'$gt': 20}}, {'age': {'$lt': 60}}]})`

## Exercicio 3.1

Resposta de cada questao seguir a sequencia de comandos

### `db.stocks.find({ "Profit Margin" : { '$gte': 0.5 } }).limit(10)`
### `db.stocks.find({ "Profit Margin" : { '$lte': 0.5 } }).limit(10)`
### `db.stocks.find().sort({ "Profit Margin" : -1}).limit(10)`
### `db.stocks.find().sort({ "Profit Margin" : -1}).limit(1)`
### `db.stocks.find().sort({ "Profit Margin" : -1})`
### `db.stocks.updateMany({}, {$rename: {"Profit Margin": "profit"}})`
### `db.stocks.aggregate([{ '$project' : { 'Ticker' : 1, 'profit' : 1 } }] )`
### `db.stocks.find().sort({ "Performance (Year)" : -1}).limit(3).pretty()`
### `db.stocks.aggregate([{ '$group': { 'Sector': { '$avg': {'$profit' } } } }] )`

## Exercicio 3.2

Resposta de cada questao seguir a sequencia de comandos
### `db.stocks.distinct('sender')`
### `db.stocks.countDocuments({ 'text': {'$regex' : ".*fraud*"}})`
