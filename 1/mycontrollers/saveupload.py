#!/usr/bin/env python
# coding: utf-8
import web
import uuid
import random
import time
import sae.storage
from config import settings
from datetime import datetime

render = settings.render

class SaveUpload:
    def GET(self):
        # 初始化一个Storage客户端。
        s = sae.storage.Client()
        imagelist=s.list('pythondb')
        return render.SaveUpload(imagelist)

    # def GET(self):
    #     web.header("Content-Type","text/html; charset=utf-8")
    #     return """<html><head><title>文件上传并且保存demo</title></head><body>
    #                 <form method="POST" enctype="multipart/form-data" action="">
    #                 <input type="file" name="myfile" />
    #                 <br/>
    #                 <input type="submit" />
    #                 </form>
    #                 </body></html>"""

    def POST(self):
        x = web.input(myfile={})
        if 'myfile' in x:
            #读取所有文件内容
            imagevalue=x.myfile.file.read()
            # 初始化一个Storage客户端。
            s = sae.storage.Client()

            # 设置object的属性
            ob = sae.storage.Object(imagevalue)
            #保存文件
            saveuploadfile= str(time.time()) + str(random.random())+x.myfile.filename
            s.put('pythondb',saveuploadfile, ob)

        raise web.seeother('/todo/saveupload')