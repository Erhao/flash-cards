from typing import Optional
from pydantic import root_validator
from datetime import datetime
from odmantic import Model, Field
from bson import ObjectId

from app.model.base import BaseMongoModel


class Category(Model, BaseMongoModel):
    """
    类别
    """
    id: int = Field(primary_field=True, description="id")
    name: str = Field(description="类别名称")
    updated_at: datetime = Field(default=datetime.utcnow())
    created_at: datetime = Field(default=datetime.utcnow())
