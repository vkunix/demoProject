from django.forms import ModelForm
from .models import DemoClass

class DemoClassForm(ModelForm):
    
    class Meta:
        model = DemoClass
        fields = ['name']