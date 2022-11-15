from flask import Flask, request, jsonify, render_template
from utils import HousePrice
import config
import numpy as np
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict_home_price():

    data = request.form

    sqrt  = eval(data["sqrt"])
    bath  = int(data["bath"])
    bhk   = int(data["bhk"])
    location = data["location"]

    house = HousePrice(sqrt, bath, bhk, location)
    price = house.predict_house_price()

    return render_template("index2.html", house_price = np.round(price, 2)[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUM1)
    