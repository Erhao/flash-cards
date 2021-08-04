# -*- coding: utf-8 -*-
from app.model.card import FlashCard


class FlashCardServ:
    """
    卡片
    """
    async def create(self, docs):
        print('----------------docs', docs)
        card = FlashCard(**docs)
        return await card.save()

    async def update(self, _id, front_content):
        card_record: FlashCard = await FlashCard.get_from_oid(_id)
        if not card_record:
            raise(Exception("卡片未找到"))

        doc = {
            "front_content": front_content,
        }
        return await card_record.update(doc)


flashcard_serv = FlashCardServ()
