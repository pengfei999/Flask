from flask import Flask, jsonify
from werkzeug.utils import redirect


'''

格式：redirect("地址"),地址既可以是本服务器的地址也可以是其它服务器的地址
注意点：重定向的代号是302
特点：重定向是两次请求
'''


app=Flask(__name__)


#自动导包，alt+enter
@app.route("/jingdong")
def jingdong():
    #跳转到淘宝去
    return redirect("http://www.taobao.com")

if __name__ == '__main__':
    app.run(debug=True)