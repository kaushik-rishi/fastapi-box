from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.myDB
users_collection = db.usersCollection

users_collection_find = users_collection.find()

insert_one_called = 0


def insert_user(user_obj):
    global insert_one_called
    # print("called @ ", insert_one_called)
    inserted_user = users_collection.insert_one(user_obj)
    # print(inserted_user.inserted_id)
    insert_one_called += 1


def get_users():
    users = []
    for user in users_collection_find:
        users.append(user)
    return users


def test_document_count():
    users_count = users_collection.count_documents({})
    print("users_count: ", users_count)


users_list = []

for i in range(100000):
    users_list.append({
        "name": f"rishi {i}",
        "age": i
    })

from time import perf_counter

start_time = perf_counter()
for user in users_list:
    insert_user(user)

end_time = perf_counter()
print(end_time - start_time)

# test_document_count()
