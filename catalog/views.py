from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Product, Contact
from catalog.forms import ProductForm, VersionForm
from catalog.services import get_categories


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        # categories = get_categories()
        for product in products:
            product.active_version = product.versions.filter(is_active=True).first()
        # context['categories'] = categories
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        new_product = form.save()
        new_product.owner = self.request.user
        new_product.save()
        selected_version = form.cleaned_data['version']
        selected_version.products.add(new_product)
        selected_version.save()
        return super().form_valid(form)


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
    context_object_name = 'product'

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return get_object_or_404(Product, name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        product.active_version = product.versions.filter(is_active=True).first()
        context['product'] = product
        return context