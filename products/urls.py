from django.urls import path

from .views import ShowAllProducts

from products import views

urlpatterns = [
    path('', views.ShowAllProducts, name='showProducts'),
    path('product/<int:pk>', views.productDetail, name='productDetail'),
    path('Add-Product/', views.addProduct, name='addProduct'),
    path('Update/<int:pk>', views.updateProduct, name='updateProduct'),
    path('Delete/<int:pk>', views.deleteProduct, name='deleteProduct'),
    path('search/', views.searchBar, name='search'),

]