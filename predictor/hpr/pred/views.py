from django.shortcuts import render
import pandas as pd
import numpy as np


# Create your views here.
def index(request):
    return render(request, 'index.html')


def predict_price(location, area, bathroom, bhk):
    X = pd.read_csv("X.csv")
    p=X.drop(['Unnamed: 0'], axis = 'columns')
    model = pd.read_pickle(r"C:\Users\ADITYA\Documents\GitHub\new_model.pickel")

    loc_index = np.where(p.columns == location)[0][0]

    x = np.zeros(len(p.columns))
    x[0] = area
    x[1] = bathroom
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]


def predict_chance(request):
    area = float(request.GET.get('area'))
    city = request.GET.get('city')
    bhk = int(request.GET.get('bhk'))
    bothroom = float(request.GET.get('bothroom'))

    result = predict_price(city, area, bothroom, bhk)
    return render(request, 'result.html', {'result': result})
