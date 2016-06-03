from __future__ import unicode_literals


import os
from django.db import models
from django.db.models.signals import post_save, post_delete
# Create your models here.

import shutil
## TODO will modify for aws3 and make environment variables
temp_upload_to = 'media/temp/%s'
upload_to = 'media/surveys/%s/%s'
delete_path = 'media/surveys/%s'


class CustomFileError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
         
def _get_upload_to(instance, filename):
    if not ( filename.endswith('.pdf') or filename.endswith('.xlsx') or filename.endswith('.csv') ):
        raise CustomFileError("file needs to have a pdf or xlsx extension")
    print "passed exception"
    return temp_upload_to % (filename)
    
class Survey(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    file = models.FileField(upload_to= _get_upload_to) # to validate file type http://blog.hayleyanderson.us/2015/07/18/validating-file-types-in-django/
    contents_file = models.FileField(upload_to= _get_upload_to)
  
    
    
    def __unicode__(self):
		return self.title

# class TableOfContents(models.Model):
    




	
	
# signal to save file post_save	
def upload_file(sender, instance, created, **kwargs):
    # disconnect to prevent recursion of signal 
    # after editing the survey instance
    post_save.disconnect(upload_file, sender=Survey)
    
    # get temporary file saved file path 
    get_file_path = instance.file.url
    get_contents_file_path = instance.contents_file.url
    # get the id of the survey
    directory = "media/surveys/%s" % (instance.id)

    # see if the folder exists or not for that post id
    # if the file exists do nothing 
    # if it does not exist create the folder in /media/surveys with the id as the folder name
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)  
       
    # from IPython import embed; embed()   
    # move the file from temporary location to new location i.e /media/surveys/4
    move_file_path = upload_to%(instance.id,instance.file.url.split('/')[-1])
    move_contents_file_path = upload_to%(instance.id,instance.contents_file.url.split('/')[-1])
    
    shutil.move(get_file_path, move_file_path)
    shutil.move(get_contents_file_path, move_contents_file_path)
    # edit the instance so it has the new file path
    instance.file = move_file_path
    instance.contents_file = move_contents_file_path
    instance.save()

    print "Post save emited for", instance

    post_save.connect(upload_file, sender=Survey)
    
# loads pdf files into media directory
# and saves the survey instance so it has new file path
post_save.connect(upload_file, sender=Survey)
    


def delete_file(sender, instance, **kwargs):
    
    # get temporary file saved file path 
    get_file_path = instance.file.url
    remove_folder = delete_path % ( instance.id)
    try:
        shutil.rmtree( remove_folder )
    except:
        print("could not find: %s"%(remove_folder))
# deletes file  dispatch_uid="gallery.image.file_cleanup"
post_delete.connect(delete_file, sender=Survey)