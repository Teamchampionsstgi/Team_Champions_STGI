import pickle
import json
import pyrebase
import urllib


# return json template

def return_json(data , status , message):

    msg = {
    'status': status,
    'message': message, 
    'data': data 
    }

    return json.loads( json.dumps(msg))

# make connection

def makeconnection():
    config = {

        "apiKey": "AIzaSyB9sv78P0NNDCJZo_ajyT9WW9KN6ijJ7go",
        "authDomain": "pec-stgi-hackathon.firebaseapp.com",
        "databaseURL": "https://pec-stgi-hackathon-default-rtdb.firebaseio.com",
        "projectId": "pec-stgi-hackathon",
        "storageBucket": "pec-stgi-hackathon.appspot.com",
        "messagingSenderId": "308456257581",
        "appId": "1:308456257581:web:1a5239999035b4a332e0a4",
        "measurementId": "G-RNNQXFELPJ"
    }
    firebase = pyrebase.initialize_app(config)
    return firebase

# create realtime database instance 

def create_realtime_instance():

    fb = makeconnection()
    db = fb.database()
    return db

# create storeage database instance

def create_storage_instance():

    fb = makeconnection()
    st = fb.storage()

    return st

# fetch model from storage
   
def get_model():

    st = create_storage_instance()
    classifier_link = st.child(f"classifier.pickle").get_url(None)
    classifier=  urllib.request.urlopen(classifier_link)
    classifier= pickle.load(
        classifier)
    return (classifier )


def writepickle(data ):
    
    f = open(f'classifier.pickle' , 'wb+')
    f.write(pickle.dumps(data))
    f.close()

def write_model():
   
   st = create_storage_instance()
   st.child(f'classifier.pickle').put(f'classifier.pickle')
