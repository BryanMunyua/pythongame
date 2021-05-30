import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("COOP.csv")

print(data.head())
data = data[["Date","Price"]]