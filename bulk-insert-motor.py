import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("localhost", 27017)

db = client.myDB
users_collection = db.usersCollection

users_collection_find = users_collection.find()

insert_one_called = 0


async def insert_user(user_obj):
    global insert_one_called
    # print("called @ ", insert_one_called)
    inserted_user = await users_collection.insert_one(user_obj)
    # print(inserted_user.inserted_id)
    insert_one_called += 1
    return inserted_user


def get_users():
    users = []
    for user in users_collection_find:
        users.append(user)
    return users


def test_document_count():
    users_count = users_collection.count_documents({})
    print("users_count: ", users_count)


async def main():
    users_list = []

    for i in range(100000):
        users_list.append({
            "name": f"rishi {i}",
            "age": i
        })

    from time import perf_counter

    insert_promises = []

    start_time = perf_counter()
    for user in users_list:
        insert_promises.append(insert_user(user))

    results = await asyncio.gather(*insert_promises)
    # print(results)

    end_time = perf_counter()
    print(end_time - start_time)


if __name__ == "__main__":
    asyncio.run(main())
