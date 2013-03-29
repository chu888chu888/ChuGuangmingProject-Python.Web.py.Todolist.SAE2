#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from sae.mail import send_mail
render = settings.render


class send:
    def POST(self):
        session = web.config._session
        access_token = session.get('access_token', None)
        if access_token == 'true':
            i = web.input()
            email = i.get('email', None)
            detail = i.get('msg', None)
            #不加下面这行Content-Type会出错的
            send_mail("5211486@qq.com", email, detail,
                      ("smtp.sina.cn", 25, "chinapython@sina.cn", "chinapython", False))
            web.header("Content-Type", "text/html;charset=utf-8")
            return "OK"
        else:
            return render.error('您没有登录，请登录', '/todo/login')
    def GET(self):
        session = web.config._session
        access_token = session.get('access_token', None)
        if access_token == 'true':
            return "OK"
        else:
            return render.error('您没有登录，请登录', '/todo/login')