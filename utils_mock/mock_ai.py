import flask, json
from flask import request

# 创建接口后台服务，方便请求接口
server = flask.Flask(__name__)  # 把app.python文件当做一个server

server.config['JSON_AS_ASCII'] = False


# ai 动作接口调用
@server.route('/ai/action', methods=['get', 'post'])
def print_request_body():
    response = '{"name":"陈翩"}'
    data = json.loads(response)
    print(data)
    if data is None:
        return "body is null"
    return data


# mock 发送短信的接口，此接口用于接收短信
@server.route('/ai/sms', methods=['get', 'post'])
def print_request_body_01():
    data = json.loads(request.get_data(as_text=True))
    print("botai请求参数：\n", data)
    if data is None:
        return "body is null"
    return data


# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(host="0.0.0.0", port=9000, debug=True)
