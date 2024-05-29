from django.forms import ModelForm
from django import forms
from .models import Locations, Incident, FireStation

class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"

class IncidentForm(ModelForm):
    date_time = forms.DateField(
        label="Incident Date",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Incident
        fields = "__all__"


class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"
