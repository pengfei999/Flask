"""
返回响应（字符串）
-1直接返回响应体数据
-2直接返回响应体数据+状态码
-:return "字符串状态码

-3直接返回响应体数据+状态码+响应头信息
-:return"字符串“ ，状态码，｛”key“：”value“｝


"""

from flask import Flask

app=Flask(__name__)
@app.route("/")
def helloword():
    # -1
    # 直接返回响应体数据
   # return "helloword"
    # -2
    # 直接返回响应体数据 + 状态码
    #return 'helloword',666

    # -3
    # 直接返回响应体数据 + 状态码 + 响应头信息
    # -:
    # return "字符串“ ，状态码，｛”key“：”value“｝
    return 'helloword6666', 666,{"Content-Type":"application/json999","name":"pengfei"}



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)