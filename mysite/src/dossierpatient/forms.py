from django import forms
from .models import DossierPatient


class DossierPatientForm(forms.ModelForm):
    class Meta:
        model   = DossierPatient
        fields  = ['nom_patient' , 'sexe' , 'date_de_naissance']