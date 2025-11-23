from pymongo import MongoClient  #connects to mongodb server
from config.settings import Settings

settings = Settings()

_client = MongoClient(settings.MONGO_DB_URL, tz_aware=True)  #tz--> timezone
_db = _client[settings.MONGO_DB_NAME]

def get_collection(name: str):
    return _db[name]
