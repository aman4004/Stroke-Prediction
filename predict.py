from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# model
model = pickle.load(open('SVC_model.p', 'rb'))
scaler = StandardScaler()

# Input format:
inpfmt = ['age', 'hypertension', 'bmi',
          'work_type_Self-employed', 'work_type_children']


# model to make prediction
def predictor(data):
    data = np.array(data).reshape(1, -1)
    data = scaler.fit_transform(data)

    result = model.predict(data)
    if result == [1]:
        print('\nPrediction: Stroke Patient\n')
    else:
        print('\nPrediction: Non-Stroke Patient\n')


# user input
inp = eval(
    input(f"Enter a list in following format\n{str(inpfmt)}\nYour input: "))
predictor(inp)
