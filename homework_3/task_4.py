from uuid import uuid4
from hashlib import sha256

class CacheObject:
    def __init__(self, cache, limit=None, salt=uuid4().hex):
        self.cache = set(cache)
        self.limit = limit
        self.salt = salt
        if limit and len(cache) > limit:
            raise UserWarning(f'Кеш не помещается, не влезает {len(cache)-limit} объектов')

    def caching(self, url):
        if sha256(url.encode() + self.salt.encode()).hexdigest() in self.cache:
            print(f'Страница {url} присутствует в кэше объекта {self}')
        else:
            result = sha256(url.encode() + self.salt.encode()).hexdigest()
            self.cache.add(result)
            print(self.cache)

myCache = CacheObject({}, 10)

myCache.caching('www.google.com')
myCache.caching('www.google.com')