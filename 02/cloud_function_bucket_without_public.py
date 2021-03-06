import requests
import pickle
from google.cloud import storage

def classifier(request):
    
    if request.method == 'GET':
        return "Welcome to Classifier"
    
    if request.method == 'POST':
        
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('sheyda-classifier-models')
        data = request.get_json()
        
        if data['model'] == ['DecisionClassifier']:
            blob = bucket.blob('models/decision_tree_model/model.pkl')
            blob.download_to_filename('/tmp/model.pkl')
            model = pickle.load(open('/tmp/model.pkl', 'rb'))
            x_data = data['x']
            output = model.predict(x_data)
            pred_class = 'Text:' + str(x_data) + '\nPredicted class is : ' + str(output)
            
        elif data['model'] == ['LinearSVC']:
            blob = bucket.blob('models/linear_svc_model/model.pkl')
            blob.download_to_filename('/tmp/model.pkl')
            model = pickle.load(open('/tmp/model.pkl', 'rb'))
            x_data = data['x']
            output = model.predict(x_data)
            pred_class = 'Text:' + str(x_data) + '\nPredicted class is : ' + str(output)
            
        else:
            blob = bucket.blob('models/logistic_regression_model/model.pkl')
            blob.download_to_filename('/tmp/model.pkl')
            model = pickle.load(open('/tmp/model.pkl', 'rb'))
            x_data = data['x']
            output = model.predict(x_data)
            pred_class = 'Text:' + str(x_data) + '\nPredicted class is : ' + str(output)
            
    return pred_class