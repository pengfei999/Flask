from flask  import Flask

app=Flask(__name__)

#替换：ctrl+r


#在访问路由的时候指定参数
#格式：@app.route("/<类型：变量名>")
#常见的参数类型：
# 1、整数：int
# 小数：float
# 字符串：path（默认为path）

@app.route("/<float:number>")

def get_float(number):

    return "this float is %s"%number

@app.route("/<int:number>")

def get_int(number):

    return "this int is %s"%number

@app.route("/<number>")

def get_string(number):

    return "this path is %s"%number


if __name__ == '__main__':
    print(app.url_map)
    app.run(host = "127.0.0.1",port = 5001,debug=True)
