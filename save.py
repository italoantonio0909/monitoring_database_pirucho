from bson.objectid import ObjectId
import pandas
import os
import datetime
from dotenv import load_dotenv
from pyrsistent import field
from config import collections_dict

load_dotenv()

DATABASE = os.environ.get("DATABASE")

DATABASE_NAME = os.environ.get("DATABASE_NAME")


def get_database():
    from pymongo import MongoClient
    import pymongo
    # from bson import ObjectId

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = DATABASE

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[DATABASE_NAME]


def data_to_csv(*, directory, data, headers):

    today = datetime.datetime.now()
    today_format = today.strftime("%d-%m-%y %H:%M")

    base_dir = os.path.abspath('..')
    donwload_dir = os.path.join(
        base_dir, "respaldo-pirucho", directory.title(), today_format)

    if not os.path.exists(donwload_dir):
        os.makedirs(donwload_dir, exist_ok=True)

    filename_to_save_xls = os.path.join(
        donwload_dir, f"{directory}-respaldo-{today_format}.xls")

    filename_to_save_csv = os.path.join(
        donwload_dir, f"{directory}-respaldo-{today_format}.csv")

    df = pandas.DataFrame(
        data, columns=headers)

    df.to_csv(filename_to_save_xls, index=False)
    df.to_csv(filename_to_save_csv, index=False)


if __name__ == "__main__":

    collections = [
        "users",
        "baseusers",
        "transactions",
        "coupons",
        "organizations",
        "branchoffices"
    ]

    connection = get_database()

    for collection_name in collections:

        data = []

        ref = collections_dict.get(collection_name)

        collection_ref = connection[collection_name]

        for collection in collection_ref.find():

            rows = []

            for field in ref.get("fields"):
                collection_field = collection.get(field, None)

                if collection_field is not None:
                    rows.append(collection_field)

            data.append(rows)

        headers = [header for header in ref.get("headers")]

        data_to_csv(
            directory=ref.get("directory"),
            data=data,
            headers=headers
        )

        print(f"Saved data {collection_name}")

    collection = connection["users"]
    users = collection.find({"base_user": {"$regex": "^((?!string).)*$"}})
    counter = 0

    for e in users:
        _id = e.get('_id')
        base_user = e.get('base_user')
        counter += 1

        collection.find_one_and_update({"_id": _id}, {"$set": {"base_user": ObjectId(base_user)}})

        print("User data sanned ", base_user)
