from .forms import HouseForm 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import Houses 
from .serializer import HousesSerializers 

import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 

class CustomerView(viewsets.ModelViewSet): 
    queryset = Houses.objects.all() 
    serializer_class = HousesSerializers 

def status(df):
    try:
        # scaler=pickle.load(open("/Users/HP-k/DeployML/DjangoAPI/Scaler.sav", 'rb'))
        model=pickle.load(open("C:\\Users\\Afsul Rahman\\Documents\\Data Science\\Project\\Linear Regression\\House PricePrediction\\banglore_home_prices_model.pickle", 'rb'))
        # X = scaler.transform(df) 
        print(model,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=--=-=-=-=-")
        y_pred = model.predict([df]) 
        return y_pred 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView(request):
    if request.method=='POST':
        form=HouseForm(request.POST or None)

        if form.is_valid():
            location = form.cleaned_data['location']
            sqft = form.cleaned_data['sqft']
            bathroom = form.cleaned_data['bathroom']
            bedroom = form.cleaned_data['bedroom']
            df=[location,sqft,bathroom,bedroom]
            print(df,"This is form 7878787877878787877")
            # df=pd.DataFrame({'location':[location], 'sqft':[sqft], 'bathroom':[bathroom], 'bedroom':[bedroom]})
            result = status(df)
            return render(request, 'status.html', {"data": result}) 
            
    form=HouseForm()
    return render(request, 'form.html', {'form':form})