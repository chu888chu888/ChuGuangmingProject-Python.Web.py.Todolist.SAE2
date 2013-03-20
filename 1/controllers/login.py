#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
render = settings.render
def myloadhook():
    global session
    session = web.config._session
class LoginUser:
    def GET(self):
        return render.LoginUser()
class CheckUser:
    def POST(self):
        #获取Session相关信息
        myloadhook()
        #获取表单信息
        i = web.input()
        username =i.get('txtUserName',None)
        password=i.get('txtUserPass',None)
        #从全局配置文件中得到session
        session = web.config._session
        if username == 'chu888' and password == 'chu888':
            session.access_token = 'true'
            raise web.seeother('/')
        else:
            session.access_token = 'false'
            raise web.seeother('/todo/login')