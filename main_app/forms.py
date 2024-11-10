from django import forms
from .models import Vehicle, MaintenanceWork


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["make", "model", "year", "vin"]


class MaintenanceWorkForm(forms.ModelForm):
    class Meta:
        model = MaintenanceWork
        fields = [
            "name",
            "miles_at_work",
            "product_link",
            "part_number",
            "price_of_work",
            "notes",
            "date_of_service",
        ]
        widgets = {
            "date_of_service": forms.DateInput(
                attrs={"type": "date"}
            ), 
        }
