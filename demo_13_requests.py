

from flask import Flask


'''
request.data:获取非表单（ajax）以post，提交的数据；
request.form：获取的表单已post方式提交数据
request.args:获取的是问好后面的查询参数
request.method:获取请求方式
request.files:获取的是input标签中type类型为file的文件
'''


app=Flask(__name__)


#自动导包，alt+enter
@app.route("/")
def jingdong():

    pass

if __name__ == '__main__':
    app.run(debug=True)