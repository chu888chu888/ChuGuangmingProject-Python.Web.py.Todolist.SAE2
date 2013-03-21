#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from dboperation import useroper

render = settings.render


class LoginUser:
    def GET(self):
        return render.LoginUser()


class CheckUser:
    def POST(self):
        #获取表单信息
        i = web.input()
        username = i.get('txtUserName', None)
        password = i.get('txtUserPass', None)
        #从全局配置文件中得到session
        session = web.config._session
        #从数据库判断用户是否存在
        if useroper.UserInfoTableOperation.checkuserlogin(self, username, password):
            session.access_token = 'true'
            raise web.seeother('/')
        else:
            session.access_token = 'false'
            raise web.seeother('/todo/login')