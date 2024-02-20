from sql import User
from sql import session

class User_service:
    def add_user(name,password):
        user=User(name=name,password=password)
        session.add(user)
        session.commit()
        return True
    def check(name,password):
        res=session.query(User).filter(User.name==name,User.password==password).first()
        session.commit()
        print(res)
        if res:
            return True
        else:
            return False