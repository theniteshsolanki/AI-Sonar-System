#IMPORTING LIBRARIES AND FUNCTIONS
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Data collection and storing
sonar_data = pd.read_csv("sonar-data.csv", header=None) #since are data file have no header we use header = none 

print(sonar_data.head())#first five rows of data

