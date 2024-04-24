from app.api.models import EngineerIn, EngineerOut
from app.api.db import engineers, database


async def add_engineer(payload: EngineerIn):
    query = engineers.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_engineer():
    query = engineers.select()
    return await database.fetch_all(query=query)


async def get_engineer(id):
    query = engineers.select().where(engineers.c.id == id)
    return await database.fetch_one(query=query)


async def delete_engineer(id: int):
    query = engineers.delete().where(engineers.c.id == id)
    return await database.execute(query=query)

