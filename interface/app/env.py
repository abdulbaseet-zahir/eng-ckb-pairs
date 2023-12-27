import os
import dotenv

dotenv.load_dotenv()

CONFIG_PATH = os.getenv("CONFIG_PATH")
MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")
