from typing import Optional
from pydantic import root_validator
from datetime import datetime
from odmantic import Model, Field

from app.model.base import BaseMongoModel
from app.constants.user import GENDER_TYPE_LIST, UNKNOWN
from app.model.card import FlashCard
from app.constants.card import FLASH_CARD_INSPIRATION, FLASH_CARD_KNOWLEDGE, FLASH_CARD_TIMER, FLASH_CARD_COMMEMORATE


class User(Model, BaseMongoModel):
    """
    user
    """
    openid: Optional[str] = Field(description="openid")
    mobile: Optional[str] = Field(description="电话")
    name: Optional[str] = Field(description="姓名")
    gender: int = Field(default=UNKNOWN, description="性别")
    is_del: int = Field(default=0, description="是否删除")
    updated_at: datetime = Field(default=datetime.utcnow())
    created_at: datetime = Field(default=datetime.utcnow())

    @root_validator
    def check_gender(cls, values):
        _gender = values['gender']
        if _gender not in GENDER_TYPE_LIST:
            raise ValueError(f"gender should be in {GENDER_TYPE_LIST}")
        return values

    class Config:
        collection = "user"

    async def create_welcome_cards(self):
        """
        新用户注册时自动创建介绍性卡片. 灵感卡 知识卡 倒计时卡 纪念卡
        :return:
        """
        inspiration_card = {
            "front_content": "一句深夜的生活感喟\n一个富有诗意的镜头表现手法\n一幅个性值点满的设计图稿\n...",
            "back_content": "灵光一现的感觉交由`灵感卡`记录",
            "type": FLASH_CARD_INSPIRATION,
            "creator": self.id,
        }
        knowledge_card = {
            "front_content": "地铁上刷知乎?\n公交刷微博?\neverywhere刷抖音?",
            "back_content": "碎片化时间里还可以记亿点`知识卡`(支持markdown哦~)",
            "type": FLASH_CARD_KNOWLEDGE,
            "creator": self.id,
        }
        timer_card = {
            "front_content": "女朋友'亲戚'还有三天就要来看她了\n回家之前记得买些特产带回去\n一个月后有一个技能考试\n...",
            "back_content": "不是Todo list, `倒计时卡`只是想给你一个规划生活的小地方",
            "type": FLASH_CARD_TIMER,
            "creator": self.id,
        }
        commemorate_card = {
            "front_content": "结婚纪念日\n工作后第一次发工资的日子\n甚至是阿猫阿狗的生日",
            "back_content": "让`纪念卡`记着, 是因为心里有",
            "type": FLASH_CARD_COMMEMORATE,
            "creator": self.id,
        }
        await FlashCard(**inspiration_card).save()
        await FlashCard(**knowledge_card).save()
        await FlashCard(**timer_card).save()
        await FlashCard(**commemorate_card).save()
