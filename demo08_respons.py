from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["get"])
def helloword():
    return "helloword,thinkyou!",666,{"Content-Type":"application/json"}



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)