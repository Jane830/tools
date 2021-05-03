import flask, json
from flask import request

# 创建接口后台服务，方便请求接口
server = flask.Flask(__name__)  # 把app.python文件当做一个server

server.config['JSON_AS_ASCII'] = False


# 装饰器，将get_all_user()函数变为一个接口 127.0.0.1:9000/get_user
@server.route('/get_user', methods=['get', 'post'])
def get_all_user():
    all_user = [
        {'id': 1, 'sex': 1, 'real_name': '小花'},
        {'id': 2, 'sex': 0, 'real_name': '小明'},
        {'id': 3, 'sex': 0, 'real_name': '小黑'}
    ]
    res = json.dumps(all_user, ensure_ascii=False)  # 将list转换为json串，ensure_ascii为False时，可以包含non-ASCII字符
    return res


@server.route('/ai/action', methods=['get', 'post'])
def print_request_body():
    # data = json.loads(request.get_data(as_text=True))
    str = '{"name":"陈翩"}'
    print(str)

    data = json.loads(str)
    postForm = request.form

    getArgs = request.args

    postValues = request.values

    print("botai请求参数：\n", getArgs)

    if data is None:
        return "body is null"
    return data




# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(host="0.0.0.0", port=9000, debug=True)
