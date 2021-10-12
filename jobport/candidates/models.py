# Create your models here.

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone

#from candidates.managers import UserManager

GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

"""
test comment
# commenting out for now, can be used in future to teach how to customize built in User Model

class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={"required": "Role must be provided"})
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    #objects = UserManager() # could be used in future for custom manager.

 """


class Country(models.Model):
    country_code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)


class Candidates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #it saves email or id?
    full_name = models.CharField(max_length=100)
    dob = models.DateTimeField(default=timezone.now)
    permanent_address = models.CharField(max_length=300)
    communication_address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=56)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, default='Male', null=True)
    mobile = models.CharField(max_length=15)
    resume = None
    looking_for = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    skills = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=2)


    #job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="candidates")
    #title = models.CharField(max_length=300)
    #bio = models.TextField()
    #age = models.SmallIntegerField()
    #certificate_issuing_country = models.CharField(max_length=56) # will switch to countryfield or enums laer
    #have_passport = models.BooleanField(default=True) #  choices can be used too
    #valid_us_visa = models.BooleanField(default=False) # choices can be used as well based on need
    

    class Meta:
        ordering = ["id"]
        #unique_together = ["user", "job"] # will use UniqueConsraint

    def __str__(self):
        return self.user.get_full_name()

    @property
    def get_status(self):
        if self.status == 1:
            return "Pending"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"


'''
Skills, Nationality, Age, Certificate issuing country, Having Passport (Yes/No), Valid US Visa - (Yes/No)



Sorting as per age, Passport status, Visa status [also years of experience, could be useful right?]

'''


class Passport(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=50)
    issuing_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    place_of_issue = models.CharField(max_length=50)
    date_expires = models.DateTimeField(default=timezone.now) 


class Visa(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    visa_type = models.CharField(max_length=50)
    provider_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=timezone.now)
    #need_visa_sponsor = None


class Certificates(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    country_issued = models.ForeignKey(Country, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(default=timezone.now)
    
    #url = models.CharField(max_length=500)
    #provider = None
    