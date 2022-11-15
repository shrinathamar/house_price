import numpy as np
import pickle
import json
import config

class HousePrice():

    def __init__(self, sqrt, bath, bhk, location):
        self.sqrt = sqrt
        self.bath = bath
        self.bhk  = bhk
        self.location = location

    def load_model(self):

        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JASON_PATH, "r") as f:
            self.columns = json.load(f)

    def predict_house_price(self):
        self.load_model()

        test_array = np.zeros(len(self.columns["data_columns"]))

        test_array[0] = self.sqrt
        test_array[1] = self.bath
        test_array[2] = self.bhk
        idx_loc = self.columns["data_columns"].index(self.location)
        test_array[idx_loc]

        price = self.model.predict([test_array])
        return price
