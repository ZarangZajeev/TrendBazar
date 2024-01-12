from django.urls import path
from api import views

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("products",views.ProductView,basename="products")
router.register("baskets",views.BasketView,basename="basket")
router.register("baskets/item",views.BasketItemView,basename="basketitems")

urlpatterns=[
    path('register/',views.SiginUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
]+router.urls