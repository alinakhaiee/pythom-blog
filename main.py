from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from config import Config

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://newuser:123456@localhost/test_main'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

@app.route('/',methods=['POST'])
def index():
    data = request.json
    print("dddata",data)
    return "okkkk"
    # action=request.args.get('ac')
    # username=request.args.get('name')
    # password=request.args.get('pass')
    # if action and password and username:
        
    #     if action.lower()=='register':
    #         new_use=User()
    #         new_use.username=username
    #         new_use.password=password
    #         db.session.add(new_use)
    #         db.session.commit()
    #         return "added user"
    #     if action.lower()=='login':
    #         user=User.query.filter(User.username==username, User.password==password).first()
    #         if not user:
    #             return"invalid"
    #         return f"welcom {user.username}"
    # else:
    #     return "hello word"
