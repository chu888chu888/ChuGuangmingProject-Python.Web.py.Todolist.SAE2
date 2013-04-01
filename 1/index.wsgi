#!/usr/bin/env python
# coding: utf-8
import web
import sae
from config.url import urls
from config import settings

render = settings.render
# You can use template result like below, either is ok:
#return web.notfound(render.notfound())
#return web.notfound(str(render.notfound()))
def notfound():
    #return web.notfound("对不起你要查询的页面不存在")
    return web.notfound(render.notfound())


def internalerror():
    return web.internalerror("服务器错误")

#是否具有调试功能
web.config.debug = True
#解决Session在SAE中的问题
app = web.application(urls, globals())
#加入404与505
app.notfound = notfound
app.internalerror = internalerror
#将session保存在数据库中
db = settings.db
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store)
web.config._session = session
#启动服务器
application = sae.create_wsgi_app(app.wsgifunc())


