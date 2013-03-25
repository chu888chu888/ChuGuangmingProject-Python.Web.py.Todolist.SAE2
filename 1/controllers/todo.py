#!/usr/bin/env python
# coding: utf-8
import web

from config import settings
from dboperation import useroper

render = settings.render


class New:
    def POST(self):
        i = web.input()
        title = i.get('title', None)
        detail = i.get('content', None)
        #获取用户ID
        session = web.config._session
        userinfo = session.get('userinfo', None)
        userid = userinfo["id"];
        if not title:
            return render.error('标题是必须的', None)
        useroper.TodoTableOperation.insert(self, title, userid, detail)
        raise web.seeother('/')


class Finish:
    def GET(self, id):
        session = web.config._session
        userinfo = session.get('userinfo', None)
        userid = userinfo["id"];
        todo = useroper.TodoTableOperation.get_by_id(self, id, userid)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        status = i.get('status', 'yes')
        if status == 'yes':
            finished = 1
        elif status == 'no':
            finished = 0
        else:
            return render.error('您发起了一个不允许的请求', '/')
        useroper.TodoTableOperation.updatefinish(self, finished, id, userid)
        raise web.seeother('/')


class detail:
    def GET(self, id):
        session = web.config._session
        access_token = session.get('access_token', None)
        if access_token == 'true':
            detaillist = useroper.TodoTableOperation.selectorderbyDetail(self, id)
            return render.detail(detaillist)
        else:
            return render.error('您没有登录，请登录', '/todo/login')


class Edit:
    def GET(self, id):
        session = web.config._session
        userinfo = session.get('userinfo', None)
        userid = userinfo["id"];
        todo = useroper.TodoTableOperation.get_by_id(self, id, userid)
        if not todo:
            return render.error('没找到这条记录', None)
        return render.todo.edit(todo)

    def POST(self, id):
        session = web.config._session
        userinfo = session.get('userinfo', None)
        userid = userinfo["id"];
        todo = useroper.TodoTableOperation.get_by_id(self, id, userid)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        title = i.get('title', None)
        if not title:
            return render.error('标题是必须的', None)
        content=i.get('content',None)
        useroper.TodoTableOperation.updatetitle(self, title, id, userid,content)
        return render.error('修改成功！', '/')


class Delete:
    def GET(self, id):
        session = web.config._session
        userinfo = session.get('userinfo', None)
        userid = userinfo["id"];
        todo = useroper.TodoTableOperation.get_by_id(self, id, userid)
        if not todo:
            return render.error('没找到这条记录', None)
        useroper.TodoTableOperation.delete(self, id, userid)
        return render.error('删除成功！', '/')


class Index:
    def GET(self):
        session = web.config._session
        access_token = session.get('access_token', None)
        if access_token == 'true':
            userinfo = session.get('userinfo', None)
            userid = userinfo["id"]
            todos = useroper.TodoTableOperation.selectorder(self, userid)
            return render.index(todos)
        else:
            return render.error('您没有登录，请登录', '/todo/login')


class reset:
    def GET(self):
        session = web.config._session
        session.kill()
        raise web.seeother('/todo/login')
