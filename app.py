from flask import Flask , render_template , request , redirect ,flash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/" , methods=['GET' , 'POST'])
def base():
    
    if request.method=='POST':
        return("Congo Team Champions")   

@app.route("/time" , methods=['GET' , 'POST'])
def time():
    
    if request.method=='POST':
        return("Time is correct for you")   
