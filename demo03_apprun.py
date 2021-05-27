from flask  import Flask

app=Flask(__name__)


#在访问路由的时候指定参数

#常见的参数类型 1、整数：int  小数：float 字符串：path（默认为path）

@app.route("/")

def index():
    return "<h1>this is flask2</h1>"


if __name__ == '__main__':
    print(app.url_map)
    #debug设置为ture有两个好处，
    # 1、如果运行的过程中，直接改了代码，不需要重新启动程序，只要ctrl+s保存即可部署程序
    # 2、如果程序报错了会有友情提示

    app.run(host = "127.0.0.1",port = 5001,debug=True)