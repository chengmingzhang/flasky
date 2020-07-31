import pymongo


class MongoInfo:
    def __init__(self):
        self.client = pymongo.MongoClient(host='202.53.138.35', port=27017)
        self.collection = self.client['biquge']['xuanhuan_and_xiuzhen']

    def find(self):
        book20 = self.collection.find().limit(20)
        return book20

    def update(self, item):
        self.collection.insert_one(item)

    def remove(self, item):
        self.collection.remove(item)

    def close(self):
        self.client.close()