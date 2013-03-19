#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
render = settings.render
class LoginUser:
    def GET(self):
        return render.LoginUser()