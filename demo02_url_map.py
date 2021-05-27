'''
查看哪些路由（地址）可有访问
一格式：使用app.url_map，返回的是装饰器的所有路由地址和路径之间的映射关系
-注意点：只有被app.url_map包含进来的路由才能被访问
'''




from flask import Flask

app=Flask(__name__)

#绑定路由与映射函数的关系
@app.route("/")
def index():
    return "this is index"

@app.route("/haha")
def index2():
    return "<h1>this is index2</h1>"


#启动app
if __name__ == '__main__':
    print(app.url_map)
    app.run()