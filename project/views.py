
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
    json_data = BASE_NUEL_URL
    query = request.GET.get('search')
    json_data = json_data.json()

    json_data =json_data['items']
   
    context ={'json_data':json_data,'query':query}
    return render(request,'search.html',context)   
         
    


def sea(request):
    json_data = BASE_NUEL_URL.text
    query = request.GET.get('search')
    json_obj = json.loads(json_data)
   
    if query in json_obj.items():

        output_dict = [x for x in json_obj if x['tags'] == query]
        output_json = json.dumps(output_dict)
    

        data =json_data['items']
        for issues in data:
            context ={'issues':issues}
   
        info=issues
        for item in issues['tags']:
            if query in item:
                print(query)

    return render(request,'search.html') 







def check(request):
    json_data = requests.get(BASE_NUEL_URL)
    query = request.GET.get('search')

    for data in json_data.json()['items']:
        if data['answer_count'] ==0:
            title =data['title']
            link = data['link']
            context ={
                'title':title,
                'link':link
            }
            return render(request,'search.html',context)

        else:
            pass
        return render(request,'search.html')



    



def contactMe(request):
  

    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']
       # products_name =request.POST['property']
        products = request.POST.getlist('property')




        # seend a mail
        # the order in which  to  pass arugument in the parameters is important
        send_mail(
            message_name , # email subject
            #message_phone, #phone no
            message_email , # from email 
            message ,      # main message
            #products, # items

            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
        
        #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = message_phone
        contacts.email = message_email
        contacts.selected_properties = products
        contacts.message = message
        contacts.save()


        return render(request ,'email.html',{'message_name' :message_name}) 

    else:
        return render(request ,'contact.html') 