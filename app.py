from flask import Flask,request, url_for, redirect, render_template, jsonify
#from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

#model = load_model('deployment_28042020')
cols = ['age', 'sex', 'color_of_skin','respiratory_rate','use_of_accessory_muscles','lung_auscultation','brain_function','heart_rate']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    print(int_features)
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    #prediction = predict_model(model, data=data_unseen, round = 0)
    #prediction = int(prediction.Label[0])
    print(data_unseen)
    return render_template('home.html',pred='Expected Bill will be 1000')
    

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data = request.get_json(force=True)
#     data_unseen = pd.DataFrame([data])
#     prediction = predict_model(model, data=data_unseen)
#     output = prediction.Label[0]
#     return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
