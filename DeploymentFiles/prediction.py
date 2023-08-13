#Python test file for Flask to predict locally
from flask import Flask, jsonify
import requests as r
import pandas as pd
import json

base_url = 'http://127.0.0.1:5000/' #base url for local host 

json_data = {
'is_banked':0,
'code_module_x':0,
'code_presentation_x':0,
'gender':0,
'region':6,
'highest_education':0,
'imd_band':4,
'age_band':0,
'num_of_prev_attempts':2,
'code_module_y':0,
'code_presentation_y':0,
}

test = pd.read_csv('Xtest.csv', index_col=0)
test = test.to_json(orient='records')
test = json.loads(test)



#Get response
#response = r.post(base_url + 'predict', json=json_data)
response = r.post(base_url + 'predict', json= test)

if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print('request failed')
    #print('Response content:', response.content)