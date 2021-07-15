from typing import Optional
from pydantic import root_validator
from datetime import datetime
from odmantic import Model, Field

from app.model.base import BaseMongoModel
from app.constants.user import GENDER_TYPE_LIST, UNKNOWN


class User(Model, BaseMongoModel):
    """
    user
    """
    openid: Optional[str] = Field(description="openid")
    mobile: Optional[str] = Field(description="电话")
    name: str = Field(description="姓名")
    gender: str = Field(default=UNKNOWN, description="性别")
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
