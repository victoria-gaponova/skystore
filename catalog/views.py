from django.shortcuts import render

from catalog.models import Product, Contact


# Create your views here.
def home(request):
    context = {
        'title': 'SkyStore',
        'products': Product.objects.all()[:6]

    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    context = {
        'title': 'Contacts',
        'contact': Contact.objects.first()

    }
    if request.method == 'POST':
        visiter = {}
        visiter["name"] = request.POST.get('name')
        visiter["phone"] = request.POST.get('phone')
        visiter["message"] = request.POST.get('message')
        print(visiter)
    return render(request, 'catalog/contacts.html', context=context)
