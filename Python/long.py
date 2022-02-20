import redis

class Redis:

    def __init__(self, db=0):
        self.db = db
        self.data = {self.db: {}}

    def get(self, key):
        """Gets the value associated with a key"""
        return self.data.get(self.db, {}).get(key)
    def set(self, key, value):

        """Sets a key-to-value association"""
        self.data[self.db][key] = value
        return True
    def delete(self, key):

        """Deletes a key"""
        del self.data[self.db][key]
        return True

r = redis.Redis(host='localhost', port=6379, db=[])
r.set('Hello', 'World')
value = r.get('Hello')
print(value)