#!/usr/bin/env python
# coding: utf-8
import os
import sae
from config.url import urls
import web
web.config.debug = True
app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)
