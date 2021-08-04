# -*- coding: utf-8 -*-
from app.model.user import User


class UserServ:
    """
    用户
    """
    async def wx_register(self, openid):
        """
        注册openid
        :param openid:
        :return:
        """
        user = await User.find_one({"openid": openid})
        if user:
            return user

        user = User(openid=openid)
        return await user.save()


user_serv = UserServ()
