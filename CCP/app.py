from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("churn_model.pkl", "rb"))
feature_columns = pickle.load(open("columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_form", methods=["POST"])
def predict_form():
    data = {col: float(request.form.get(col, 0)) for col in feature_columns}
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    return render_template("result.html", prediction=int(pred), probability=round(prob, 3))

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    df = pd.DataFrame([data]).reindex(columns=feature_columns, fill_value=0)
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]
    return jsonify({"churn_prediction": int(pred), "churn_probability": float(prob)})

if __name__ == "__main__":
    app.run(debug=True)
