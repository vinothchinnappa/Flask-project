import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    x1 = data['feature1']
    x2 = data['feature2']
    result = 0.8 * x1 + 0.2 * x2
    return jsonify({
        "predicted_value": result,
        "lower_bound": result - 5,
        "upper_bound": result + 5,
        "explanation": "Prediction driven mostly by feature1"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default for local
    app.run(host='0.0.0.0', port=port)
