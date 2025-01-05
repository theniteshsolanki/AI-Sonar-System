#IMPORTING LIBRARIES AND FUNCTIONS
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Data collection and storing
sonar_data = pd.read_csv("sonar-data.csv", header=None) #since are data file have no header we use header = none 

# # print(sonar_data.head())#first five rows of data
# print(sonar_data.shape)#dimensions of data
# # print(sonar_data.describe())#discrioption of data
# print(sonar_data[60].value_counts())

sonar_data.groupby(60).mean()
X = sonar_data.drop(columns = 60, axis = 1) 
Y = sonar_data[60]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)