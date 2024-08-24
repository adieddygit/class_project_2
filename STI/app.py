from flask import Flask, render_template, url_for, session
from sqlalchemy import create_engine, text
from models.models import *

app = Flask(__name__)

connection_string = "mysql+mysqlconnector://root:@wsl.localhost/STI"
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)

Person.__table__.create(engine, checkfirst=True)
with engine.connect() as connection:
   
    connection.commit()

@app.route('/')

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
