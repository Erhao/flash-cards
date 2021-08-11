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
        record = await User.find_one({"openid": openid})
        if record:
            return record

        record = User(openid=openid)
        user = await record.save()

        # 给新用户创建四个介绍性卡片
        await user.create_welcome_cards()

        return user


user_serv = UserServ()
