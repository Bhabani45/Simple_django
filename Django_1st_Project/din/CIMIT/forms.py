from django import forms
from CIMIT.models import Venue

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels ={
           'name' : "Employee Name",
           "password": "Password",
           "Emailid": "Email_Id"



        }