from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':"매트릭스"})
print(movie['star'])
target_star = movie['star']
target_movies = list(db.movies.find({'star':str(target_star)},{'_id':False}))
for star in target_movies:
    print(star['title'])

db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': 0}})

