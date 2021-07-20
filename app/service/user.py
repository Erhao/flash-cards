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
        is_exist = await User.find_one({"openid": openid})
        if is_exist:
            return {}

        user = User(openid=openid)
        return await user.save()


user_serv = UserServ()
