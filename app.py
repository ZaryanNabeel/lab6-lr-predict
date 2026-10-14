import random
from flask import Flask, request, jsonify

STUDENT_ROLL_NUMBER = 39
REGISTRATION_NUMBER = "FA23-BDS-039"

seed = STUDENT_ROLL_NUMBER
random.seed(seed)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args.get("x1", 0))
        x2 = float(request.args.get("x2", 0))
        x3 = float(request.args.get("x3", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "x1, x2 and x3 must be numeric"}), 400
    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({
        "registration number": REGISTRATION_NUMBER,
        "prediction": round(y, 2)
    })

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "Linear Regression Prediction API",
        "registration number": REGISTRATION_NUMBER,
        "usage": "/predict?x1=2&x2=3&x3=1"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
