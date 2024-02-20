from routes import app
from flask import render_template,request

from services.user import User_service


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.post('/api/login')
def Login():
    data = request.get_json()
    name = data['username']
    password = data['password']
    res=User_service.check(name,password)
    if res:
        return {
            'code':0,
            'message':'登录成功'
        }
    else:
        return {
            'code':-1,
            'message':'登录失败'
        }