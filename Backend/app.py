from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load your ML model
model = joblib.load('fish_predictor_model.pkl')

# Example: serve Goa ocean data
@app.route('/data', methods=['GET'])
def get_data():
    df = pd.read_csv('goa_daily_salinity.csv')
    return jsonify(df.to_dict(orient='records'))

# ML prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        salinity = float(data['salinity'])
        temperature = float(data['temperature'])

        prediction = model.predict([[salinity, temperature]])
        return jsonify({'fish_present': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
