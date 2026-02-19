from pymongo import mongo_client
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017'
    MONGO_INITDB_DATABASE: str = ''
    COLLECTION_NAME: str = 'orders'

    REDIS_HOST: str = 'localhost'
    KAFKA_HOST: str = 'localhost:9092'
    class Config:
        env_file = './.env'


settings = Settings()


def _connection():
    client = mongo_client.MongoClient(settings.DATABASE_URL)
    print('Connected to MongoDB...')
    return client

def _db(client):
    db = client[settings.MONGO_INITDB_DATABASE]
    return db
 
def get_collection(collection_name):
    conn = _connection()
    db = _db(conn)
    coll = db[collection_name]
    return coll