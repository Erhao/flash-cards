# -*- coding: utf-8 -*-
from bson import ObjectId
from fastapi import APIRouter, Depends

from app.db.mongodb import AsyncIOMotorClient, get_database


router = APIRouter()


@router.get("/test")
async def test(db: AsyncIOMotorClient = Depends(get_database)):
    """
    测试
    :return:
    """
    couriers = db['aoao-lite']['courier'].find()
    print('-----------------------------------0')
    async for row in couriers:
        print('----------', row["name"])
    print(couriers)  # Cursor
    print('-----------------------------------1')
    return {"ok": 1}


@router.get("/test2")
async def test2(db: AsyncIOMotorClient = Depends(get_database)):
    """
    测试
    :return:
    """
    courier = await db['aoao-lite']['courier'].find_one({"_id": ObjectId("6081350270893a3ab1177fe5")})
    print('-----------------------------------0')
    print(courier)  # Cursor
    print('-----------------------------------1')
    return {"ok": 1}


@router.get("/get")
async def get():
    # print('-----------------------card id()', id(db))
    # print('----------------------router db', db)
    # courier_records_count = await db.courier.find_one({"name": "测试111"})
    # print('----------------------c', courier_records_count)
    return
