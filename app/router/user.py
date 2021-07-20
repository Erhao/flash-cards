# -*- coding: utf-8 -*-
import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.db.mongodb import AsyncIOMotorClient, get_database, get_aio_engine
from app.core.config import database_name, wx_app_id, wx_app_secret
from app.model.user import User
from app.model.tag import Tag


router = APIRouter()


class WxRegisterReq(BaseModel):
    """

    """
    code: str


@router.post("/wx/register")
async def wx_register(req: WxRegisterReq):
    """
    微信小程序code换session
    :return:
    """
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={wx_app_id}&secret={wx_app_secret}&js_code={req.code}&" \
          f"grant_type=authorization_code"
    res = requests.get(url)
    print(res)

