# -*- coding: utf-8 -*-
from typing import List, Optional
from fastapi import APIRouter, Depends
from odmantic import AIOEngine, ObjectId
from pydantic import BaseModel

from app.db.mongodb import AsyncIOMotorClient, get_database, get_aio_engine
from app.core.config import database_name
from app.model.card import FlashCard
from app.model.tag import Tag
from app.service.card import flashcard_serv


router = APIRouter()


class UpsertReq(BaseModel):
    """

    """
    id: Optional[str]
    front_text: Optional[str]
    back_text: Optional[str]


@router.get("/test")
async def test(db: AsyncIOMotorClient = Depends(get_database)):
    """
    测试
    :return:
    """
    cards = db[database_name]['flash_card'].find()
    print('-----------------------------------0')
    async for row in cards:
        print('----------', row["back_content"])
    print(cards)  # Cursor
    print('-----------------------------------1')
    return {"ok": 1}


@router.get("/test_odmantic")
async def test_odmantic():
    """
    测试
    :return:
    """
    # print('-----------------------------------0')
    # # card = await engine.find_one(FlashCard, {"tag": 10})
    # card: FlashCard = await FlashCard.find_one({"tag": 10})
    # print('-------------------------card', card)
    # print(card.front_content)
    # print(card)  # Cursor
    # print('-----------------------------------1')
    # doc = {
    #     "back_content": "new content2"
    # }
    # res = await card.update(doc)
    # print('-------------------------res', res)

    # cards: List[FlashCard] = await FlashCard.find({"tag": 10})
    # print('-----------------cards', cards)
    # for card in cards:
    #     print(card.front_content)
    #     print(card.created_at)

    # new_card = FlashCard(
    #     front_content="123",
    #     back_content="456",
    #     creator=ObjectId("6065413270893a83895965a3")
    # )
    # print('-------------------------new_card', new_card)
    # await engine.save(new_card)

    # tag = Tag(
    #     id=12,
    #     name="test"
    # )
    # print('------------tag', tag)
    # await tag.save()
    
    return {"ok": 1}


@router.get("/get")
async def get():
    return

@router.post("/upsert")
async def upsert(req: UpsertReq):
    # 创建
    if not req.id:
        docs = dict()
        if req.front_text:
            docs['front_content'] = req.front_text
        if req.back_text:
            docs['back_content'] = req.back_text
        res = await flashcard_serv.create(docs)
    # 更新
    else:
        pass
    return res
