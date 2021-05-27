

from flask import Flask

app=Flask(__name__)
print(__name__)
print(app.static_url_path)
print(app.static_folder)
print(app.template_folder)


#使用app，通过路由绑定一个视图函数
#函数一定要有返回值
@app.route("/")

def helloword():
    return "helloword Flask"


if __name__ == '__main__':
    #运行app程序
    app.run()
    print("haha")
