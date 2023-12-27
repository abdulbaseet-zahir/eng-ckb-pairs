from datetime import datetime
import os

import dotenv
import pandas as pd
import pymongo

dotenv.load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATA_PATH = os.getenv("DATA_PATH")


def insert_data_into_mongodb(
    data_path, mongo_url, database_name, collection_name, limit=None, clean=False
):
    """
    Inserts data from a CSV file into a MongoDB collection.

    Args:
        data_path (str): Path to the CSV file containing the data.
        mongo_url (str): URL of the MongoDB server.
        database_name (str): Name of the MongoDB database.
        collection_name (str): Name of the MongoDB collection.
        limit (int, optional): Maximum number of rows to insert.
    """

    data = pd.read_csv(data_path, sep="\t", nrows=limit)

    client = pymongo.MongoClient(mongo_url)
    db = client[database_name]
    collection = db[collection_name]

    if clean:
        collection.delete_many({})

    try:
        for _, row in data.iterrows():
            filter = {"eng_id": row["eng_id"], "ckb_id": row["ckb_id"]}
            update = {
                "$set": {
                    "eng_sentence": row["eng_sentence"],
                    "ckb_sentence": row["ckb_sentence"],
                    "eng_username": row["eng_username"],
                    "ckb_username": row["ckb_username"],
                    "reviewed": False,
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
            }
            collection.update_one(filter, update, upsert=True)

    except pymongo.errors.PyMongoError as e:
        print(f"Error occurred during MongoDB operation: {e}")

    finally:
        client.close()


def main():
    insert_data_into_mongodb(
        DATA_PATH, MONGO_URL, DATABASE_NAME, "tatoeba", limit=10, clean=False
    )


if __name__ == "__main__":
    main()
