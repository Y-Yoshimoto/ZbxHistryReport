# coding: utf-8
import requests
import json
import random

import timeperiod
# https://qiita.com/sti320a/items/f20b8cbc06bf70425d33


class zabbixRequest():
    ZabbixURL = "null"  # Zabbix Webサーバ URL
    authKey = None  # 認証キー <class 'str'>

    def __init__(self, user, password, url):
        self.ZabbixURL = url
        # 認証用リクエストデータ生成
        # https://www.zabbix.com/documentation/4.0/manual/api/reference/user/login
        requestParams = {"user": user, "password": password}
        # リクエスト生成 認証キー取り出し
        self.authKey = self.__reqZabbix("user.login", requestParams)["result"]

    def __reqZabbix(self, method, requestParams):
        # リクエスト生成,送信
        requestData = {
            "jsonrpc": "2.0",
            "method": method,
            "params": requestParams,
            "id": random.randrange(1000),
            "auth": self.authKey
        }
        # print(" - sendData: ", end="")
        # print(requestData)  # <class 'dict'>
        response = requests.post(
            self.ZabbixURL,
            data=json.dumps(requestData),
            headers={'Content-Type': 'application/json-rpc'})
        # print(response.status_code)
        # print(" - responseData: ",end=""); print(json.loads(response.text))  # <class 'dict'>
        return json.loads(response.text)

        # https://www.zabbix.com/documentation/4.0/manual/api/reference_commentary#common_get_method_parameters
    def HistoryGet(self, id, time_from, time_till):
        # https://www.zabbix.com/documentation/4.0/manual/api/reference/history/get
        requestParams = {
            "output": "extend",
            "history": 0,
            "itemids": id,
            "sortfield": "clock",
            "sortorder": "ASC",
            "time_from": time_from,
            "time_till": time_till
        }
        return self.__FormatHistory(
            self.__reqZabbix("history.get", requestParams)['result'])

    def __FormatHistory(self, result):
        re = []
        for item in result:
            item.update(timeperiod.convertToDayDate(int(item['clock'])))
            item.pop('ns')
            re.append(item)
        return re

def HistoryGet(environ, start_response):
    print('HistoryGet')
    start_response('200 OK', [('Content-Type', 'application/json')])
    query = environ.get('QUERY_STRING')
    print(query)

    itemids = 10073
    ## Zabbix接続インスタンス生成
    myinstance = zabbixRequest("Admin", "zabbix",
                               "http://192.168.1.7/zabbix/api_jsonrpc.php")
    ## 取得期間設定
    yesterday = timeperiod.timeperiod().Yesterday()
    ## ヒストリー取得
    history = myinstance.HistoryGet(itemids, yesterday["unixTime_from"],
                                    yesterday["unixTime_till"])
    # print(json.dumps(history, sort_keys=True, indent=4))
    ## レスポンスデータ生成
    sendData = json.dumps(history, ensure_ascii=False).encode('utf-8')
    # sendData = json.dumps(history,sort_keys=True,indent=4,ensure_ascii=False).encode('utf-8')

    # print(sendData)
    return sendData
    ## curl -X GET "http://127.0.0.1:3380/api_py/historyget?itemids=10073" > respons.json