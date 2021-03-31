class RedisRepository:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def exists(self, key):
        return self.redis_client.exists(key)

    def get(self, key):
        return self.redis_client.get(key)

    def put(self, key, value):
        return self.redis_client.set(key, value)

    def delete(self, key):
        return self.redis_client.delete(key)

class MongoRepository:
    def __init__(self, mongo_db):
        self.db = mongo_db

    def get(self, key):
        res = self.db.find_one({"key":key})
        if (res != None):
            return res['value']

    def put(self, key, value):
        return self.db.insert_one({"key" : key, "value":value})    

    def delete(self, key):
        return self.db.remove({"key":key})