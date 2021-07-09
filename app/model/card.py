from typing import Optional
from pydantic import root_validator
from datetime import datetime
from odmantic import Model, Field
from bson import ObjectId

from app.model.base import BaseMongoModel
from app.constants.card import FLASH_CARD_KNOWLEDGE, FLASH_CARD_TYPE_LIST


class FlashCard(Model, BaseMongoModel):
    """
    flash-card
    """
    front_content: str = Field(description="前面文本")
    back_content: str = Field(description="背面文本")
    category: Optional[int] = Field(description="类别")
    tag: Optional[int] = Field(description="标签")
    type: int = Field(default=FLASH_CARD_KNOWLEDGE, description="类型")
    is_private: int = Field(default=1, description="是否私有")
    creator: ObjectId = Field(description="创建者")
    is_del: int = Field(default=0, description="是否删除")
    updated_at: datetime = Field(default=datetime.utcnow())
    created_at: datetime = Field(default=datetime.utcnow())

    @root_validator
    def check_type(cls, values):
        _type = values['type']
        if _type not in FLASH_CARD_TYPE_LIST:
            raise ValueError(f"type should be in {FLASH_CARD_TYPE_LIST}")
        return values

    class Config:
        collection = "flash_card"
