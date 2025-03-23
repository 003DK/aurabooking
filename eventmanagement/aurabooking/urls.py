from django.urls import path
from . import views
urlpatterns=[
    path("",views.login,name = 'login'),
    path("register/",views.register,name = 'register'),
    path("guest/",views.guest,name='guest'),
    path("eventhost/",views.event,name='eventmanager'),
    path("eventhost/create",views.create,name='createeventr'),
    path("guest/eventdetails/",views.details,name='details'),
    path("guest/eventdetails/payment",views.payment,name='payments')

]