import sys
sys.path.append("../src")
from flask import Flask,request,render_template
from make_full_poem import make_poems

app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return "Hello "+name

@app.route('/redi/')
def redi():
    return render_template('hello.html')

@app.route('/redi2/<name>')
def redi2(name):
    return render_template('hello2.html',name=name)

@app.route('/met',methods=['GET','POST'])
def met():
    if request.method=='GET':
        poems = make_poems("端",7)
        return poems
    if request.method=='POST':
        return '这是POST方法'

if __name__ == '__main__':
    app.run()