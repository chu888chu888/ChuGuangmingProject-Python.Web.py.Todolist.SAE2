#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/', pre_fix + 'todo.Index',
    '/todo/new', pre_fix + 'todo.New',
    '/todo/(\d+)', pre_fix + 'todo.View',
    '/todo/(\d+)/edit', pre_fix + 'todo.Edit',
    '/todo/(\d+)/delete', pre_fix + 'todo.Delete',
    '/todo/(\d+)/finish', pre_fix + 'todo.Finish',
    '/todo/(\d+)/detail', pre_fix + 'todo.detail',
    '/todo/login', pre_fix + 'login.LoginUser',
    '/todo/checkuser', pre_fix + 'login.CheckUser',
    '/todo/reguser', pre_fix + 'login.RegUser',
    '/todo/reset', pre_fix + 'todo.reset',
    '/todo/sendmail', pre_fix + 'sendemail.send',
    '/warringie6', pre_fix + 'warring.WarringIE6',
    '/todo/saveupload', 'mycontrollers.saveupload.SaveUpload'
)
