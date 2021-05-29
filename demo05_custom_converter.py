'''

背景：
如果系统提供的int，float，等参数类型满足不了需求的时候，我们需要自定义
之所以int，float。path，可以接收不同的数据类型，是因为，系统提供了好的对应转换器了
-自定义转换器格式
-1、定义类，继承自BaseConver
-2、重写init方法
-3、初始化父类 成员变量，还有子类自己的规则
-4、将状换器类，添加到系统默认的转换器列表中
'''
from flask import Flask
from werkzeug.routing import BaseConverter

app=Flask(__name__)


# -1、定义类，继承自BaseConver
class MyRegxConverter(BaseConverter):
    #这样直接指定不够灵活，具体应该匹配什么规则应该交给路由
    #regex = "\d{3}"
    pass
'''
    # -2、重写init方法,接收两个参数
    def __init__(self,map,regex):
        #-3.初始化父类成员变量，还有子类自己的规则
        super(MyRegxConverter, self).__init__(map)
        self.regex=regex
'''
    # -3、初始化父类 成员变量，还有子类自己的规则

    # -4、将状换器类，添加到系统默认的转换器列表中
app.url_map.converters["re"]=MyRegxConverter
#打印出所有的转换器：
print(app.url_map.converters)


#匹配3位整数
#使用re（“规则”）实际上是传递了两个参数，参数1：url_map参数2括号中写的正则规则

@app.route('/<re:number>')

def get_three(number):

    return "this number is three %s"%number
'''

#匹配4位整数
@app.route('/<re("\d{4}"):number>')

def get_four(number):

    return "this number is four %s"%number

#匹配手机号位整数
@app.route('/<re("1[3-9]\d{9}"):number>')

def get_phone_number(number):

    return "this phone number is  %s"%number
'''
if __name__ == '__main__':
    app.run(debug=True)
    print(666)