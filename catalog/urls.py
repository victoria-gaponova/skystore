from django.urls import path

from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('product/сreate/', ProductCreateView.as_view(), name='create_product')
]
