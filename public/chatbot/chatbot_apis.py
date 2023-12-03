from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask (__name__)

@app.get("/")
def index_get():
    return "Server is Running"

@app.post ("/predict")
def predict():
    text = request. get_json ().get ("message")
    # TODO: check if text is valid
    response = get_response (text)
    message = {"answer": response}
    print("Data received at predict")
    return jsonify (message)


if __name__ == "__main__":
    # app. run (debug=True)
    app.run(host='127.0.0.1', port=5000 , debug=True)