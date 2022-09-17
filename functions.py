
from pickle import GET
import app_database
import json
import numpy as np
import re

# return template

def return_json(data , status , message):

    msg = {
    'status': status,
    'message': message, 
    'data': data 
    }

    return json.loads(json.dumps(msg))


# machine learning model

def model(X_train, y_train):


    from catboost import CatBoostClassifier
    
    classifier = CatBoostClassifier()
    classifier.fit(X_train, y_train , verbose=0)
    return classifier


def test(X_test, y_test, classifier):
    print("Score of model : ")
    print(classifier.score(X_test, y_test))



def get_classification(string ):

    try:
        classifier = app_database.get_model()
        ypred = classifier.predict([string])
        return return_json(
            data=ypred,
            status=1,
            message='SUCCESS'
        )
    except Exception as e:
        return return_json(
            data=0,
            status=0,
            message='FALIED'
        )


def get_para_classification(para):

    l = re.split(r"\.|\?|\!",para)
    collection = []
    replies = []
    for line in l:
        if(line) != ' ' and line != '':
            collection.append(line)
    
    print(collection)
    for i in range(0 ,len(collection)):
        replies.append(get_classification(collection[i]))

    return replies
            