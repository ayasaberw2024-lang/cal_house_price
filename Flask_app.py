# import flask ,request , jsonify 
from flask import Flask,request,jsonify
#import joblib , numpy 
import joblib
import numpy as np 


#create the flask app 
app=Flask(__name__)

#load the model 
model=joblib.load("xgb_model.pkl")

#now define the routs and endpoints 

#main page 
@app.route('/')
def home(): 
    return " the api is runing "


#prediction api 
@app.route('/predict', methods=['POST'])
def predict():
    try: 
        data=request.get_json()
        features =np.array([data['features']])
        prediction=model.predict(features)
        
        return jsonify({"prediction":float(prediction[0])   })
    except Exception as e: 
        return jsonify({"error",str(e)})

#run the server
if __name__ == "__main__" :
    app.run(debug=True) 
