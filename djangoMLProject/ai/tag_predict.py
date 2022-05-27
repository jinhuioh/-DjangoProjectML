import warnings
warnings.filterwarnings(action='ignore')
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import joblib

def load_pkl(input_data):
    pred_module = joblib.load('ai/tag_predict.pkl')
    result = pred_module.predict_proba([input_data])
    if result[0][0] == 1:
        tag = '생활/사무용품'
    elif result[0][1] == 1:
        tag = '식료품'
    elif result[0][2] == 1:
        tag = '애완용품'
    elif result[0][3] == 1:
        tag = '인테리어'
    elif result[0][4] == 1:
        tag = '취미용품'
    elif result[0][5] == 1:
        tag = '패션'
    elif result[0][6] == 1:
        tag = '화장품'
    return tag