import base64
import datetime
import hashlib
import json
import random

import requests


def base64encode(d):
    strencode = base64.b64encode(json.dumps(d, ensure_ascii=False, separators=(',', ':')).encode())
    return str(strencode, 'iso8859-1')


def get_time_format(date):
    return date.strftime("%Y-%m-%d %H:%M:%S %f")[:-3]


def get_trans_id(date):
    return "{}{}".format(int(date.timestamp() * 1000), random.randint(100000, 999999))


data = {"templateContent": {"msg": "Your yanzhengma is: 123456"}, "templateId": "01jZRer950", "msgAddress": ["17551510295"]}

date = datetime.datetime.now()
auth = {
    "APP_ID": "d56869e8ecb447adb9eca7ceac3a9840",
    "TIMESTAMP": get_time_format(date),
    "TRANS_ID": get_trans_id(date)
}


def get_token():
    raw = "APP_ID{app_id}TIMESTAMP{timestamp}TRANS_ID{trans_id}{data}{secret}".format(app_id=auth["APP_ID"],
                                                                                      timestamp=auth["TIMESTAMP"],
                                                                                      trans_id=auth["TRANS_ID"],
                                                                                      data=json.dumps(data,
                                                                                                      ensure_ascii=False,
                                                                                                      separators=(
                                                                                                      ',', ':')),
                                                                                      secret="c7d74eb2620d4176bf0de9886b47fe83")
    m = hashlib.md5(raw.encode())
    return m.hexdigest()


def get_auth():
    auth["TOKEN"] = get_token()
    return auth


headers = {"Authentication": base64encode(get_auth()), "Content-Type": "application/json;charset=UTF-8"}

if __name__ == '__main__':
   r =  requests.post(url="https://1.69.0.118/api/middlleplatform/7ETcXe/pOkSnl/v1.0",
                  headers=headers,
                  data=json.dumps(data, ensure_ascii=False, separators=(',', ':')),
                  verify=False)
   print(r.text)