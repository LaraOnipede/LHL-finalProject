# imports
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import requests
import pickle
import pandas as pd

#Wrap the app
app = Flask(__name__)
api = Api(app) #wrapping app in a restful api

#load the model
model = pickle.load(open('gradient_boosting_model.pkl', 'rb'))

#Define Api Resources
class Predict (Resource):
    
    def post(self):  #post request
        json_data = request.get_json()
        print('Received JSON data:', json_data)

        #For 1 observation
        #df = pd.DataFrame(json_data.values(), 
        #                  index = json_data.keys()).transpose()
        
        #how to take multiple observation
        df = pd.DataFrame(json_data)

        result = model.predict(df)
        return result.tolist()
    
#Assign endpoints
api.add_resource(Predict, '/predict')


#Runn api app
if __name__ == '__main__':
    app.run(debug=True)