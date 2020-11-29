from django.urls import path
from .import views

urlpatterns = [
    #path('refrigerator/',include('refrigerator.urls'))
    path('',views.top, name='top'),
    path('food_register',views.food_register, name='food_register')
]