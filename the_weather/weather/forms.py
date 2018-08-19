from django.forms import ModelForm, TextInput
from .models import Weather

class CityForm(ModelForm):
    class Meta:
        model = Weather
        fields = ["city_name",]
        widgets = {"city_name":TextInput(attrs={"class":"input","placeholder":"City Name"})}