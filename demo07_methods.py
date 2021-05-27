
"""

给路由增加其它访问方式
-格式：@app.route(“路径”，methods=["请求方式1“，”请求方式2 ，。。。。])
-如果不指定请求方式那么就默认为get请求；
"""

from flask import Flask

app=Flask(__name__)
@app.route("/",methods=["post","get"])
def helloword():
    return "helloword"



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)