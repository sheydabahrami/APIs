import os
import sys
import numpy as np
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'models/pipe_clf_checkpoint.joblib')
model = joblib.load(open(my_file, 'rb'))
model_clf = model['pipeline_clf']

@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model_clf.predict(data["x"])
    output_text = "Text:" + str(data["x"]) 
    output = "Class: " + str(prediction)
    return jsonify(output_text, output)

if __name__ == '__main__':
    app.run(port=8080, debug=True)