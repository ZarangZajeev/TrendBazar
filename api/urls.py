from django.urls import path
from api import views

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("products",views.ProductView,basename="products")

urlpatterns=[
    path('register/',views.SiginUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
]+router.urls