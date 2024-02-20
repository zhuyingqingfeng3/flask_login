from routes import app
from flask import render_template,request

from services.user import User_service


@app.post('/api/register')
def Register():
    data=request.get_json()
    name=data['username']
    password=data['password']
    res=User_service.add_user(name,password)
    if res:
        return {
            'code':0,
            'message':'注册成功'
        }
    else:
        return {
            'code':-1,
            'message':'注册失败'
        }

