from flask import Flask, jsonify

app=Flask(__name__)


#自动导包，alt+enter
@app.route("/",methods=["get"])
def helloword():

    #1.定义字典
    dict={"name":"彭飞","age":"31"}
    #return jsonify(dict)
    #2.定义字典,简易方法
    #dict={"name":"彭飞","age":"31"}
    return jsonify(name="彭飞",age=29)



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)