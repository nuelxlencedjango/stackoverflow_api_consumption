from django.urls import path
from .views import *
from .import views 




app_name ="project"

urlpatterns = [
  
    path('' ,views.home,name='home'),
    path('check/' ,views.json_dumps,name='check'),
     path('search/' ,views.search,name='search'),
]    