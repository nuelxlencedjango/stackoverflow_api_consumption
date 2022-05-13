
import re
from django.shortcuts import render,redirect ,get_object_or_404, resolve_url
from django.contrib import auth, messages
import json

import requests
from django.utils import timezone


from django.http import HttpResponse,JsonResponse, request
from django.forms import inlineformset_factory
from django.views.generic.base import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin

from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
    )
from requests.compat import quote_plus





from django.db.models import Q 

from django.core.mail import send_mail
from .models import *
from django.conf import settings
from .forms import *

answer ='https://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow'


BASE_NUEL_URL  = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
  




def home(request):
    rs = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    json_data = rs.json()

    pack_str = json.dumps(json_data['items'],indent=2)
    json_data =json_data['items']
    num =len(pack_str)

    context={
        'json_data':json_data,
        'num':num,
        'pack_str':pack_str
    }

    return render(request, 'home.html',context)




def json_dumps(request):

    response = requests.get(BASE_NUEL_URL)
    resp = response.json()
    for data in response.json()['items']:

        title=data['title']
        #link=data['links']
        date=data['creation_date']
       # name=data['displayed_name']
            

        
    #data=resp.items
    
   
    #item =response.items.dict_items
        context={
        #'link':link,
        'date':date,
        #'name':name,
        'title':title,
        #'item':item,
        'data':data,
        'resp':resp,
        'response':response,
        
    }

   #for data in response.json():

      # print(data)
      # context = {
       # 'ques':data,
       # }
    return render(request, 'data.html',context)



def search(request):
    json_data = BASE_NUEL_URL.text
    query = request.GET.get('search')
    json_obj = json.loads(json_data)
    if query in json_obj.items():
    #output_dict = [x for x in output if x['tags'] == query]
    #output_json = json.dumps(output_dict)
    

        context ={'json_data':json_data,'js':query}
    #data =json_data['items']
    #for issues in data:
     #   context ={'issues':issues}
   
        #info=issues
      #  for item in issues['tags']:
       #     if query in item:

        #        context ={'item':query,'info':item,}
    #if item:
         #       return render(request,'search.html',context)
        
    #else:
     #   messages.warning(request,'Service not available at this time')
    return render(request,'search.html',context) 




    

     
