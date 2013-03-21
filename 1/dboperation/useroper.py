#!/usr/bin/env python
# coding: utf-8
import datetime

from config import settings


class UserInfoTableOperation:
    @staticmethod
    def checkuserlogin(self, username, password):
        s = settings.db.select('users', where='name=$username and password=$password', vars=locals())
        if not s:
            return False
        else:
            return True


class TodoTableOperation:
    @staticmethod
    def get_by_id(self, todoid):
        s = settings.db.select('todo', where='id=$todoid', vars=locals())
        if not s:
            return False
        return s[0]

    @staticmethod
    def insert(self, title):
        settings.db.insert('todo', title=title, post_date=datetime.datetime.now())

    @staticmethod
    def updatefinish(self, finished, id):
        settings.db.update('todo', finished=finished, where='id=$id', vars=locals())

    @staticmethod
    def selectorder(self):
        return settings.db.select('todo', order='finished asc, id asc')

    @staticmethod
    def delete(self, id):
        settings.db.delete('todo', where='id=$id', vars=locals())

    @staticmethod
    def updatetitle(self, title, id):
        settings.db.update('todo', title=title, where='id=$id', vars=locals())