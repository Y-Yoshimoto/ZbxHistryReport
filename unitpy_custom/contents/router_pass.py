#!/usr/bin/env python
# -*- coding: utf-8 -*-
import router_func as rfunc
import zabbix_APIuse as zget

routes = [
    ('/', rfunc.get),
    ('/historyget', zget.HistoryGet),
    #('/sendjson', rfunc.sendjson),
    #('/checkdata', rfunc.checkdata),
    #('/inquirypostcode', postcode.InquiryPostcode),
]
