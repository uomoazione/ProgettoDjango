from store import views
from django.urls import path
from store.views import ProdottoDetailView
urlpatterns=[
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("prodotto/<int:pk>/", ProdottoDetailView.as_view(),
         name="dettaglio_prodotto")
]