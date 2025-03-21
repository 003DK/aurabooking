from django.urls import path
from . import views
urlpatterns =[path("",views.index,name="index"),path("contact/<int:customer_no>",views.contact,name="contact")]