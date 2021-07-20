# -*- coding: utf-8 -*-
import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.db.mongodb import AsyncIOMotorClient, get_database, get_aio_engine
from app.core.config import database_name, wx_app_id, wx_app_secret
from app.model.user import User
from app.model.tag import Tag
from app.service.user import user_serv


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
    resp = requests.get(url)
    resp_data = resp.json()  # {'session_key': 'JJP5l97e8Z99I20eijcf6g==', 'openid': 'oeoUQ47KqeSjEfjH6Ajz0uNqv8wI'}
    openid = resp_data['openid']
    res = await user_serv.wx_register(openid)
    print(res)
    return res

