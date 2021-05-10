import flask, json
from flask import request

# 创建接口后台服务，方便请求接口
server = flask.Flask(__name__)  # 把app.python文件当做一个server

server.config['JSON_AS_ASCII'] = False


# push 对接第三方接口 逻辑

@server.route('/print', methods=['get', 'post'])
def print_request_body():
    data = json.loads(request.get_data(as_text=True))
    print("bot请求参数：\n", data)

    if data is None:
        return "body is null"
    return data


@server.route('/ivr', methods=['get', 'post'])
def print_request_body_ivr():
    data = json.loads(request.get_data(as_text=True))
    print("ivr请求参数：\n", data)

    if data is None:
        return "body is null"
    return data


@server.route('/agent', methods=['get', 'post'])
def print_request_body_agent():
    data = json.loads(request.get_data(as_text=True))
    print("技能组请求参数：\n", )
    data
    if data is None:
        return "body is null"
    return data


@server.route('/outcall', methods=['get', 'post'])
def print_request_body_outcall():
    data = json.loads(request.get_data(as_text=True))
    print("手动外呼请求参数：\n", data)

    if data is None:
        return "body is null"
    return data


@server.route('/incall', methods=['get', 'post'])
def print_request_body_incall():
    data = json.loads(request.get_data(as_text=True))
    print("呼入请求参数：\n", repr(data))

    if data is None:
        return "body is null"
    return request.get_data()


# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(host="0.0.0.0", port=9000, debug=True)
