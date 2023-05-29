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


def status(location,sqft,bhk,bath):
    with open("C:\\Users\\Afsul Rahman\\Documents\\Data Science\\Project\\Linear Regression\\House PricePrediction\\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    with open("C:\\Users\\Afsul Rahman\\Documents\\Data Science\\Project\\Linear Regression\\House PricePrediction\\banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    try:
        loc_index =  __data_columns.index(location.lower())
        print("Entered into the try9999")
    except:
        return "Provide a location in banglore"
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

       
def price_prediction(request):
    json_data = '''
{
  "data_columns": [
    "total_sqft",
    "bath",
    "bhk",
    "1st block jayanagar",
    "1st phase jp nagar",
    "2nd phase judicial layout",
    "2nd stage nagarbhavi",
    "5th block hbr layout",
    "5th phase jp nagar",
    "6th phase jp nagar",
    "7th phase jp nagar",
    "8th phase jp nagar",
    "9th phase jp nagar",
    "aecs layout",
    "abbigere",
    "akshaya nagar",
    "ambalipura",
    "ambedkar nagar",
    "amruthahalli",
    "anandapura",
    "ananth nagar",
    "anekal",
    "anjanapura",
    "ardendale",
    "arekere",
    "attibele",
    "beml layout",
    "btm 2nd stage",
    "btm layout",
    "babusapalaya",
    "badavala nagar",
    "balagere",
    "banashankari",
    "banashankari stage ii",
    "banashankari stage iii",
    "banashankari stage v",
    "banashankari stage vi",
    "banaswadi",
    "banjara layout",
    "bannerghatta",
    "bannerghatta road",
    "basavangudi",
    "basaveshwara nagar",
    "battarahalli",
    "begur",
    "begur road",
    "bellandur",
    "benson town",
    "bharathi nagar",
    "bhoganhalli",
    "billekahalli",
    "binny pete",
    "bisuvanahalli",
    "bommanahalli",
    "bommasandra",
    "bommasandra industrial area",
    "bommenahalli",
    "brookefield",
    "budigere",
    "cv raman nagar",
    "chamrajpet",
    "chandapura",
    "channasandra",
    "chikka tirupathi",
    "chikkabanavar",
    "chikkalasandra",
    "choodasandra",
    "cooke town",
    "cox town",
    "cunningham road",
    "dasanapura",
    "dasarahalli",
    "devanahalli",
    "devarachikkanahalli",
    "dodda nekkundi",
    "doddaballapur",
    "doddakallasandra",
    "doddathoguru",
    "domlur",
    "dommasandra",
    "epip zone",
    "electronic city",
    "electronic city phase ii",
    "electronics city phase 1",
    "frazer town",
    "gm palaya",
    "garudachar palya",
    "giri nagar",
    "gollarapalya hosahalli",
    "gottigere",
    "green glen layout",
    "gubbalala",
    "gunjur",
    "hal 2nd stage",
    "hbr layout",
    "hrbr layout",
    "hsr layout",
    "haralur road",
    "harlur",
    "hebbal",
    "hebbal kempapura",
    "hegde nagar",
    "hennur",
    "hennur road",
    "hoodi",
    "horamavu agara",
    "horamavu banaswadi",
    "hormavu",
    "hosa road",
    "hosakerehalli",
    "hoskote",
    "hosur road",
    "hulimavu",
    "isro layout",
    "itpl",
    "iblur village",
    "indira nagar",
    "jp nagar",
    "jakkur",
    "jalahalli",
    "jalahalli east",
    "jigani",
    "judicial layout",
    "kr puram",
    "kadubeesanahalli",
    "kadugodi",
    "kaggadasapura",
    "kaggalipura",
    "kaikondrahalli",
    "kalena agrahara",
    "kalyan nagar",
    "kambipura",
    "kammanahalli",
    "kammasandra",
    "kanakapura",
    "kanakpura road",
    "kannamangala",
    "karuna nagar",
    "kasavanhalli",
    "kasturi nagar",
    "kathriguppe",
    "kaval byrasandra",
    "kenchenahalli",
    "kengeri",
    "kengeri satellite town",
    "kereguddadahalli",
    "kodichikkanahalli",
    "kodigehaali",
    "kodigehalli",
    "kodihalli",
    "kogilu",
    "konanakunte",
    "koramangala",
    "kothannur",
    "kothanur",
    "kudlu",
    "kudlu gate",
    "kumaraswami layout",
    "kundalahalli",
    "lb shastri nagar",
    "laggere",
    "lakshminarayana pura",
    "lingadheeranahalli",
    "magadi road",
    "mahadevpura",
    "mahalakshmi layout",
    "mallasandra",
    "malleshpalya",
    "malleshwaram",
    "marathahalli",
    "margondanahalli",
    "marsur",
    "mico layout",
    "munnekollal",
    "murugeshpalya",
    "mysore road",
    "ngr layout",
    "nri layout",
    "nagarbhavi",
    "nagasandra",
    "nagavara",
    "nagavarapalya",
    "narayanapura",
    "neeladri nagar",
    "nehru nagar",
    "ombr layout",
    "old airport road",
    "old madras road",
    "padmanabhanagar",
    "pai layout",
    "panathur",
    "parappana agrahara",
    "pattandur agrahara",
    "poorna pragna layout",
    "prithvi layout",
    "r.t. nagar",
    "rachenahalli",
    "raja rajeshwari nagar",
    "rajaji nagar",
    "rajiv nagar",
    "ramagondanahalli",
    "ramamurthy nagar",
    "rayasandra",
    "sahakara nagar",
    "sanjay nagar",
    "sarakki nagar",
    "sarjapur",
    "sarjapur  road",
    "sarjapura - attibele road",
    "sector 2 hsr layout",
    "sector 7 hsr layout",
    "seegehalli",
    "shampura",
    "shivaji nagar",
    "singasandra",
    "somasundara palya",
    "sompura",
    "sonnenahalli",
    "subramanyapura",
    "sultan palaya",
    "tc palaya",
    "talaghattapura",
    "thanisandra",
    "thigalarapalya",
    "thubarahalli",
    "thyagaraja nagar",
    "tindlu",
    "tumkur road",
    "ulsoor",
    "uttarahalli",
    "varthur",
    "varthur road",
    "vasanthapura",
    "vidyaranyapura",
    "vijayanagar",
    "vishveshwarya layout",
    "vishwapriya layout",
    "vittasandra",
    "whitefield",
    "yelachenahalli",
    "yelahanka",
    "yelahanka new town",
    "yelenahalli",
    "yeshwanthpur"
  ]
}
'''

    # Parse the JSON object
    data = json.loads(json_data)

    # Extract the location columns starting from the 4th column
    location_columns = data["data_columns"][3:]
    # print(location_columns,"[][][][][[[]]]")
    if request.method=='POST':
        location = request.POST.get('location')
        sqft = request.POST.get('square_feet')
        bathroom = request.POST.get('bathroom')
        bedroom = request.POST.get('bedroom')
        print(location,sqft,bathroom,bedroom,"qwqwqwqwqwqwqwqwqwqwqwqwqwqwqwqwqw")
        result = status(location,sqft,bathroom,bedroom)
        # to_split = str(result)
        # splitted_amount = to_split.split('.')
        # # Convert to crore and lakh
        # cror = int(result) / 100
        # crore = str(cror)
        # split_cr = crore.split('.')
        # print(len(splitted_amount[0]),"12121212121212121212121")
        # if len(split_cr[0]) == 3:
        #     crore_number = split_cr[0]
        #     crore_number = int(crore_number)
        #     lakhs_number = split_cr[1]
        #     lakhs_number = int(lakhs_number)
        #     print(crore_number,lakhs_number,"cr,lkhs")
        #     if crore_number >= 2 and lakhs_number >= 2:
        #         result = f"{crore_number} crores {lakhs_number} lakhs"
        #     elif crore_number < 2 and lakhs_number >= 2:
        #         result = f"{crore_number} crore {lakhs_number} lakhs"
        #     elif crore_number >= 2 and lakhs_number < 2:
        #         result = f"{crore_number} crores {lakhs_number} lakh"
        # elif len(split_cr[0]) == 2:
        #     result = f"{split_cr[1]} lakhs"


        result = "Estimated Price : "+str(result) + " Lakhs"
        return render(request, 'form.html', {"data": result,"locations":location_columns}) 
    return render(request, 'form.html',{"locations":location_columns})