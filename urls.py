
from django.urls import path , include
from . import views

urlpatterns = [
    path("", views.home),
    path("login", views.Login),
    path("signup", views.Signup),
    path("signout", views.SignOut),
    path("showproducts/<id>", views.showproducts),
    path("addtocart", views.addToCart),
    path("viewdetails/<id>", views.Viewdetails),
    path("showCart" , views.ShowCart),
    path("WishItem", views.WishItem),
    path("about" , views.aboutus),
    path("makepayment", views.makePayment),
    path("address" , views.address),
]
