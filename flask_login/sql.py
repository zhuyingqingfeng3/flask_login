from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker



# 申明基类对象
Base = declarative_base()


# 定义user表实体对象
class User(Base):
    # 定义表名
    __tablename__ = 'user'
    # 定义字段
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    password = Column(Integer)

    def __repr__(self):
        return "User(id:{},name:{},password:{})".format(self.id, self.password, self.password)

# 数据库连接初始化
class MysqlSqlalchemy(object):
    def __init__(self):
        # 创建mysql连接引擎
        engine = create_engine("mysql+pymysql://root:1234@localhost/flaskdb",
                               echo=True)
        # 创建表
        Base.metadata.create_all(engine, checkfirst=True)
        # 创建mysql的session连接对象
        self.session = sessionmaker(bind=engine)()

session = MysqlSqlalchemy().session
# if __name__ == '__main__':
#     # 初始化mysql数据库连接，获取session
#
#
#     # 新增一条数据
#     user = User(name='xiaoming', age=23)
#     # 以下都是语法，增删改查，改的话，是查到之后修改再提交，所有的操作最后都要提交
#     session.add(user)
#     # session.add_all(datas)
#     # result = session.query(User.id, User.name, User.age).all()
#     # query_user = session.query(User).filter_by(id=user_id).first()
#     # del_count = session.query(User).filter(User.id == user_id).delete()
#     session.commit()