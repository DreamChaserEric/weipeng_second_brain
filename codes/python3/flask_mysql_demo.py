#encoding:utf-8
from tkinter.messagebox import YES
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Ericnyjdqczy08=@127.0.0.1:3306/MyTest'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JSON_AS_ASCII']=False

db = SQLAlchemy(app)
# db = SQLAlchemy(use_native_unicode='utf8')

class test(db.Model):
    __tablename__='test'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)

@app.route('/')
def index():
    db.create_all()
    return '连接成功'

@app.route('/add/')
def add():
    test_add=test(name='test_add')
    db.session.add(test_add)
    db.session.commit()
    return '增加成功！'

@app.route('/del/')
def del_():
    test_del=test.query.filter(test.name=='test_update').first()
    db.session.delete(test_del)
    db.session.commit()
    return '删除成功！'

@app.route('/update/')
def update():
    test_update=test.query.filter(test.name=='test_add').first()
    test_update.name='test_update'
    db.session.commit()
    return '更新成功！'

if __name__=='__main__':
    app.run(host='0.0.0.0') 
    # app.run(debug=True)