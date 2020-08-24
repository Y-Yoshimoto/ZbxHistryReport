#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def get(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Unit for Wsgi is Up.   Ver 0.1"]


def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b"404 Not Found."]


'''
def sendjson(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    data = {"name": "test"}
    sendData = json.dumps(data, ensure_ascii=False)
    return sendData


def checkdata(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    wsgi_input = environ["wsgi.input"]
    content_length = int(environ.get('CONTENT_LENGTH', 0))
    fromData = wsgi_input.read(content_length)
    # 値の取りだしと判定
    number = json.loads(fromData)["number"]
    result = 0 if number >= 10 else 1
    # result = 0
    data = {'result': result}
    sendData = json.dumps(data, ensure_ascii=False)
    return sendData


def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b"404 Not Found."]
'''