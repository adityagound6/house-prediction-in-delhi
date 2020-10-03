from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Predicted
import pandas as pd


# Create your views here.
def index(request):
    return render(request, 'index.html')


def predict_chance(request):
    if request.method == 'POST':
        area=request.Post.get('area')
        city=request.POST('city')
        city = request.POST('bhk')
        boathroom=request.POST.get('bothroom')

        model = pd.read_pickle(r"C:\Users\ADITYA\Documents\Machine_Learning\predictor\hpr\new_model.pickle")
        result = model.predict([[area,city ,bhk ,bothroom]])
        return render(request,'result.html',{'result':result})
