from django.db import models
#from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='profiles',null=True, blank=True)
<<<<<<< HEAD
	bio = models.CharField(verbose_name='Biografía',null=True,blank=True)
=======
	#bio = RichTextField(verbose_name='Biografía',null=True,blank=True)
	bio = models.CharField(verbose_name='Biografía',null=True,blank=True,max_length=500)
>>>>>>> dc1274b7603ab866f129c0127e5528e6d61abe0f
	link = models.URLField(max_length=200, null=True,blank=True)


