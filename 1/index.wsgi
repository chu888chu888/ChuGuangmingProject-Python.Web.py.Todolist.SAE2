#!/usr/bin/env python
# coding: utf-8
import os
import web
import sae
from config.url import urls
from config import settings

#是否具有调试功能
web.config.debug = False
# app = web.application(urls, globals()).wsgifunc()
# application = sae.create_wsgi_app(app)

#解决Session在SAE中的问题
app = web.application(urls, globals())

#将session保存在数据库中
db = settings.db
store = web.session.DBStore(db, 'sessions')
#session = web.session.Session(app, store, initializer={'access_token': 'true'})
session = web.session.Session(app, store)
web.config._session = session

application = sae.create_wsgi_app(app.wsgifunc())


