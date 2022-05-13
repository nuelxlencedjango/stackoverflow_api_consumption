
from django.db import models

from cloudinary.models import CloudinaryField
# Create your models here.

class Search(models.Model):
    title = models.CharField(max_length=500)
    search = models.CharField(max_length = 100)
    date_searched = models.DateTimeField(auto_now_add=True, null=True)
    owner_id = models.CharField(max_length=100)
    tags = models.CharField(max_length=500)
    #owner_id = models.CharField(max_length=100)
    profile = CloudinaryField(blank=True,null=True)
    owner_name = models.CharField(max_length=200)
    owner_link = models.CharField(max_length=1000)
    is_answer = models.BooleanField(default=False)
    view_count = models.CharField(max_length=200)
    question_id = models.CharField(max_length=100)
  
    
    stflow_link = models.CharField(max_length=100)
    last_activity_date =models.CharField(max_length=100)
    creation_date = models.CharField(max_length=100)


    def __str__(self):
        return '{}'.format(self.search)


    class Meta:
        verbose_name_plural ='Searches'






 


