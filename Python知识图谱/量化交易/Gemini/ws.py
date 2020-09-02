#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/31 11:03
"""

import ssl
import websocket
import json
import base64
import hmac
import hashlib
import time


def run_heartbeat_ws():
    from api import PrimaryAPI
    # https://docs.gemini.com/websocket-api/#private-api-invocation

    def on_message(ws, message):
        print(message)

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("### closed ###")

    payload = {"request": "/v1/order/events","nonce": int(time.time()*1000)}
    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(PrimaryAPI.gemini_api_secret, b64, hashlib.sha384).hexdigest()

    ws = websocket.WebSocketApp("wss://api.sandbox.gemini.com/v1/order/events",
                                on_message=on_message,
                                header={
                                    'X-GEMINI-PAYLOAD': b64.decode(),
                                    'X-GEMINI-APIKEY': PrimaryAPI.gemini_api_key,
                                    'X-GEMINI-SIGNATURE': signature
                                })
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == '__main__':
    run_heartbeat_ws()
