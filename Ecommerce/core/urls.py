from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('order-summary/', views.OrderSummaryView.as_view(), name="order-summary"),
    path('remove-single-item-from-cart/<slug>/', views.remove_single_item_from_cart,
         name="remove-single-item-from-cart"),
]
