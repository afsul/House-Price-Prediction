from django import forms
from .models import Houses

class HouseForm(forms.ModelForm):
    class Meta:
              model = Houses
              fields = "__all__"

    location=forms.CharField(max_length=150)
    sqft=forms.IntegerField()
    bathroom=forms.IntegerField()
    bedroom=forms.IntegerField()