from django.shortcuts import render
from .models import DemoClass
form .forms import DemoClassForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DemoClassForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return render(request, "demoProject/display.html", {"form": form})
    else:
        form = DemoClassForm()
    return render(request, "demoProject/home.html", {"form": form})


def demoView(request):
    obj = DemoClass.objects.all()
    return render(request, "demoPorject/display.html", {"obj": obj})