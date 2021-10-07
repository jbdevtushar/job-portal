# Create your models here.

from django.contrib.auth.models import AbstractUser, User, Group
from django.db import models

#from candidates.managers import UserManager

GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

"""
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

 class Candidates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    bio = models.TextField()
    #job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="candidates")
    created_at = models.DateTimeField(default=timezone.now)
    skills = models.CharField()
    nationality = models.CharField()
    age = models.SmallIntegerField()
    certificate_issuing_country = models.CharField() # will switch to countryfield or enums laer
    have_passport = models.BooleanField(default=True) #  choices can be used too
    valid_us_visa = models.BooleanField(default=False) # choices can be used as well based on need
    status = models.SmallIntegerField(default=2)

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