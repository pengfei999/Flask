from flask import Flask, jsonify, url_for
from werkzeug.utils import redirect


'''

解释：称为反解析，返回的是视图函数对应的路由地址
格式：url_for("视图函数“,key=value)
'''


app=Flask(__name__)


#自动导包，alt+enter
@app.route("/jingdong")
def jingdong():
    print(url_for("taobao",token=123))
    #通过url_for找到taobao地址，然后通过redirect进行重定向
    response=redirect(url_for("taobao",token=123))
    #返回响应体对象
    return response

@app.route("/yamaxun")
def yamaxun():
    print(url_for("taobao", token=456))
    response = redirect(url_for("taobao", token=456))
    return response

@app.route("/taobao<int:token>")
def taobao(token):
    if token==123:
        return "欢迎京东用户给你打5折"
    elif token==456:
        return "欢迎亚马逊用户给你打9折"
    else:
        return "欢迎其它用户给你打9.9折"

if __name__ == '__main__':
    app.run(debug=True)