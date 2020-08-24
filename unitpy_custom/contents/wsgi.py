#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import router_func as rfunc
import zabbix_APIuse as zget
import router_pass as rpass


def application(environ, start_response):
    for path, func in rpass.routes:
        if path == environ['PATH_INFO']:
            return func(environ, start_response)

    return rfunc.not_found(environ, start_response)
