from flask import Flask,request,render_template
import pickle
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("register.html")
database={'azin':'1234','ashkan':'555','nima':'ttt','ali':'888','fatemeh':'0248','navid':'sarmad', 'amin':'ghaf', 'maryam':'785136', 'mohammad':'moh73'}

databaseNames = list(database.keys())
print(random.sample(databaseNames,3))

@app.route('/form_login',methods=['POST','GET'])
def register():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('register.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('register.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name1)

if __name__ == '__main__':
    app.run()