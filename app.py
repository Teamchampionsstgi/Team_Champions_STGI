import functions
import app_database
from flask import Flask ,render_template , request , redirect , flash
from flask_cors import CORS

app =  Flask(__name__)

CORS(app)

@app.route('/test' , methods=['GET' , 'POST'])
def test():
    return "Hi" 

