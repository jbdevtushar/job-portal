from django.db import models
from django.contrib.auth.models import AbstractUser, User

# the following model can be split in many others moderls & 
# have appropriate relations as per need

class Recruiters(models.Model):
	user = None
	job_title = None
	company_info = None
	address = None
	contact_info = None
	website = None
