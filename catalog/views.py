from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        visiter = {}
        visiter["name"] = request.POST.get('name')
        visiter["phone"] = request.POST.get('phone')
        visiter["message"] = request.POST.get('message')
        print(visiter)
    return render(request, 'catalog/contacts.html')
