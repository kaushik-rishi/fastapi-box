from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"health": "ok"}


@app.post("/user")
async def health_check():
    db.users.insert_one()
    db.usernames.insert_one()
    return {"ack": True}


@app.post("/user")
async def health_check():
    await db.users.insert_one()
    await db.usernames.insert_one()
    return {"ack": True}


@app.get("/health")
async def health_check():
    return {"health": "ok"}
