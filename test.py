# 获取设备规格属性URL
urlstr = 'curl --request GET "https://openapi.tuyacn.com/v1.0/iot-03/devices/3110664824a16018b63f/specification" --header "sign_method: HMAC-SHA256" --header "client_id: hmrjarqradeiou76xm51" --header "t: 1635136193775" --header "mode: cors" --header "Content-Type: application/json" --header "sign: 7577A353EA36687BA395C2CCFE2C058FDC29D3E00A6F9B6098B51C48FB197CEA" --header "access_token: 48307942a1de6571117d6d61a04529ba"'
# 返回结果
result = {
  "result": {
    "category": "cz",
    "functions": [
      {
        "code": "switch_1",
        "desc": "{}",
        "name": "开关1",
        "type": "Boolean",
        "values": "{}"
      },
      {
        "code": "countdown_1",
        "desc": "{\"unit\":\"s\",\"min\":0,\"max\":86400,\"scale\":0,\"step\":1}",
        "name": "开关1倒计时",
        "type": "Integer",
        "values": "{\"unit\":\"s\",\"min\":0,\"max\":86400,\"scale\":0,\"step\":1}"
      }
    ],
    "status": [
      {
        "code": "switch_1",
        "name": "开关1",
        "type": "Boolean",
        "values": "{}"
      },
      {
        "code": "countdown_1",
        "name": "开关1倒计时",
        "type": "Integer",
        "values": "{\"unit\":\"s\",\"min\":0,\"max\":86400,\"scale\":0,\"step\":1}"
      }
    ]
  },
  "success": true,
  "t": 1635136183095
}

# 获取设备支持指令集
urlstr = 'curl --request GET "https://openapi.tuyacn.com/v1.0/iot-03/devices/3110664824a16018b63f/functions" --header "sign_method: HMAC-SHA256" --header "client_id: hmrjarqradeiou76xm51" --header "t: 1635136390399" --header "mode: cors" --header "Content-Type: application/json" --header "sign: 839A7B9DB0B8E6458190A283C251FF87DE7B84A3E6E4E19819227A02498E6842" --header "access_token: 48307942a1de6571117d6d61a04529ba"'
# 返回结果
result = {
  "result": {
    "category": "cz",
    "functions": [
      {
        "code": "switch_1",
        "desc": "开关1",
        "name": "开关1",
        "type": "Boolean",
        "values": "{}"
      },
      {
        "code": "countdown_1",
        "desc": "开关1倒计时",
        "name": "开关1倒计时",
        "type": "Integer",
        "values": "{\"unit\":\"s\",\"min\":0,\"max\":86400,\"scale\":0,\"step\":1}"
      }
    ]
  },
  "success": true,
  "t": 1635136379758
}