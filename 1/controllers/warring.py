#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
render = settings.render
class WarringIE6:
    def GET(self):
        return render.warringie6()