# -*- coding: utf-8 -*-
import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.db.mongodb import AsyncIOMotorClient, get_database, get_aio_engine
from app.core.config import database_name, wx_app_id, wx_app_secret
from app.model.user import User
from app.model.card import FlashCard
from app.model.tag import Tag
from app.service.user import user_serv
from app.core.jwt import create_access_token, get_current_user
from app.router.base import ReqMeta


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
    user: User = await user_serv.wx_register(openid)
    # print(user)  # id=ObjectId('60f691519885b5f2430481a1') openid='oeoUQ47KqeSjEfjH6Ajz0uNqv8wI' mobile=None name=None gender=3 is_del=0 updated_at=datetime.datetime(2021, 7, 20, 9, 2, 58, 116000) created_at=datetime.datetime(2021, 7, 20, 9, 2, 58, 116000)
    if not user:
        # TODO: raise error
        pass
    token_data = {
        "uid": str(user.id),
        "openid": user.openid
    }
    token = create_access_token(data=token_data)
    res = {
        "token": token,
    }
    return res


@router.post("/cards")
async def get_user_cards(
    _meta: ReqMeta,
    user=Depends(get_current_user)
):
    """
    获取登录用户的卡片列表
    :param _meta:
    :param user:
    :return:
    """
    uid = user.id
    offset = _meta.page * _meta.page_size
    limit = _meta.page_size

    cards = await FlashCard.find({"creator": uid})
    return cards[offset:offset+limit]
