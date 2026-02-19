from pymongo import mongo_client
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017'
    MONGO_INITDB_DATABASE: str = 'alerts_db'
    COLLECTION_NAME: str = 'alter'
    class Config:
        env_file = './.env'


settings = Settings()

class MongoConnection:
    def _connection(self):
        self.client = mongo_client.MongoClient(settings.DATABASE_URL)
        print('Connected to MongoDB...')
        return self.client

    def _db(self,client):
        db = client[settings.MONGO_INITDB_DATABASE]
        return db 

    def get_collection(self):
        conn = self._connection()
        db = self._db(conn)
        return db[settings.COLLECTION_NAME]

    def insert_alert(self,alert):
        collection = self.get_collection()
        collection.insert_one(alert)