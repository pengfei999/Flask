

from flask import Flask, jsonify, url_for,abort


'''
-使用场景：当访问服务器资源的时候，如果找不到该资源，可以报出异常信息，使用errorhandler捕捉
-格式：abort(代号）
-格式：app.errorhandler(代号)
'''


app=Flask(__name__)


#自动导包，alt+enter
@app.route("/")
def jingdong():
    abort(404)
@app.errorhandler(404)
def page_not_find(e):
    print(e)
    return "页面找不到%s"%e


if __name__ == '__main__':
    app.run(debug=True)