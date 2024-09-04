from flask import Flask, render_template, url_for, request, session
from sqlalchemy import create_engine
from STI.models.users import Base
from STI.models.users import *


app = Flask(__name__)

connection_string = "mysql+mysqlconnector://root:@localhost/sti"
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)

Person.__table__.create(engine, checkfirst=True)
with engine.connect() as connection:
   
    connection.commit()

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST': 
        return 'do_the_login()' 
    else: return 'show_the_login_form()'

@app.route('/register', methods=['POST'])
def register():
    if request.method=='POST':
        result = request.form
        email = result['email']
        role = result['role']
        
@app.route('/Chlamy_Gono')
def Chlamy_Gono():
    return render_template('Chlamy_Gono.html')

@app.route('/CS')
def CS():
    return render_template('CS.html')

@app.route('/Hep_B')
def Hep_B():
    return render_template('Hep_B.html')

if __name__ == '__main__':
    app.run(debug=True)
