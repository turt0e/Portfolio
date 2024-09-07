from django.db import models
import os
import random

#def get_filename_ext(filepath):
#    base_name = os.path.basename(filepath)
#    name, ext = os.path.splitext(base_name)
#    return name, ext

#def upload_image_path(instance, filename):
#    new_filename = random.randint(1, 3910209312)
#    name, ext = get_filename_ext(filename)
#    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#    return "Projects/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
   # image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    website_url = models.URLField(blank=True, null=True) # for repository i assume???
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

## PILLOW WONT INSTALLLLLLLLLLLLLLLLL