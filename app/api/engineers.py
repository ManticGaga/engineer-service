from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import EngineerOut, EngineerIn
from app.api import db_manager

engineers = APIRouter()

@engineers.post('/', response_model=EngineerOut, status_code=201)
async def create_engineer(payload: EngineerIn):
    engineer_id = await db_manager.add_engineer(payload)

    response = {
        'id': engineer_id,
        **payload.dict()
    }

    return response


@engineers.get('/', response_model=List[EngineerOut])
async def get_engineers():
    return await db_manager.get_all_engineer()


@engineers.get('/{id}/', response_model=EngineerOut)
async def get_engineer(id: int):
    company = await db_manager.get_engineer(id)
    if not company:
        raise HTTPException(status_code=404, detail="engineer not found")
    return company


@engineers.delete('/{id}/', response_model=None)
async def delete_engineer(id: int):
    company = await db_manager.get_engineer(id)
    if not company:
        raise HTTPException(status_code=404, detail="engineer not found")
    return await db_manager.delete_engineer(id)