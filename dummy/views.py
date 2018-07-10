from django.shortcuts import render
from .models import DemoClass
# from .forms import DemoClassForm
# Create your views here.
def homeView(request):
    if request.method == 'POST':
        form = DemoClass()
        form.name = request.POST['en_name']
        form.save()
        return render(request, "demoProject/home.html", {"message": "data saved"})
    else:
        return render(request, "demoProject/home.html", {})


def demoView(request):
    obj = DemoClass.objects.all()
    return render(request, "demoProject/display.html", {"obj": obj})