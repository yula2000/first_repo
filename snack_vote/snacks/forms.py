from django import forms
from .models import Snack


class SnackForm(forms.ModelForm):
    class Meta:
        model = Snack
        fields = ["name", "url", "submitted_by"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "간식 이름", "class": "form-input"}),
            "url": forms.URLInput(attrs={"placeholder": "https://...", "class": "form-input"}),
            "submitted_by": forms.TextInput(attrs={"placeholder": "이름 (선택)", "class": "form-input"}),
        }
        labels = {
            "name": "간식 이름",
            "url": "링크",
            "submitted_by": "올린 사람",
        }
