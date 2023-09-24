from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact


# Create your views here.
# def home(request):
#     context = {
#         'title': 'SkyStore',
#         'products': Product.objects.all()[:6]
#
#     }
#     return render(request, 'catalog/product_list.html', context=context)

class ProductListView(ListView):
    model = Product




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


# class ContactCreateView(CreateView):
#     model = Contact
#     fields = ['title', 'contact']

# def detail_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, 'catalog/product_detail.html', context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
