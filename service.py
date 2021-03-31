import logging
import logging.config

class Service:

    def __init__(self, cache, database):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.cache = cache
        self.database = database

    def get(self, key):
        if self.cache.exists(key):
            logging.info("cache " + key)
            return self.cache.get(key)
        else:
            logging.warning("no data in cache for " + key)

        value = self.database.get(key)
        if value is not None:
            self.cache.put(key, value)
        else:
            logging.error("no data in database for " + key)
        return value

    def put(self, key, value):
        self.database.put(key, value)

    def delete(self, key):
        self.cache.delete(key)
        self.database.delete(key)