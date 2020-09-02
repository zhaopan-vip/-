#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/31 10:56
"""

import requests
import json
import base64
import hmac
import hashlib
import datetime, time


def query_primary_trades():
    from api import MasterAPI
    # https://docs.gemini.com/rest-api/#get-past-trades
    url = "https://api.sandbox.gemini.com/v1/mytrades"

    t = datetime.datetime.now()
    payload_nonce = str(int(time.mktime(t.timetuple())*1000))
    payload = {
        "request": "/v1/mytrades",
        "nonce": payload_nonce,
        "account": "primary",
        "symbol": "btcusd"
    }
    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(MasterAPI.gemini_api_secret, b64, hashlib.sha384).hexdigest()

    request_headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': MasterAPI.gemini_api_key,
        'X-GEMINI-PAYLOAD': b64,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
        }

    response = requests.post(url, headers=request_headers)

    my_trades = response.json()
    print(my_trades)


if __name__ == '__main__':
    query_primary_trades()
