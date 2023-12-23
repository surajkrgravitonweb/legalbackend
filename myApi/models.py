import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .manage import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    STAFF = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (USER, 'User')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    
    first_name = models.CharField(max_length=70, blank=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    phone_number=models.CharField(max_length=200,blank=False, default=True)
    Image=models.CharField(max_length=2322232222222,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    




class UserForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15)
    related_to = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class UserFormDocument(models.Model):
    pdf_file1 = models.FileField(upload_to='pdf_files/')
    pdf_file2 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file3 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file4 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file4 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)



class Document(models.Model):
    user_form = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='documents')
    file1 = models.FileField(upload_to='documents/', blank=True, null=True)
    file2 = models.FileField(upload_to='documents/', blank=True, null=True)
    file3 = models.FileField(upload_to='documents/', blank=True, null=True)
    file4 = models.FileField(upload_to='documents/', blank=True, null=True)
    file5 = models.FileField(upload_to='documents/', blank=True, null=True)


    def __str__(self):
        return f"{self.user_form.name}'s Document"


class AllPagesApi(models.Model):
    firstName = models.CharField(max_length=255)
    email = models.EmailField()
    contactNo = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstName} - {self.email}"
    

class UserOutput(models.Model):
    email = models.EmailField()
    pdf_file1 = models.FileField(upload_to='pdf_files/')
    pdf_file2 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file3 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file4 = models.FileField(upload_to='pdf_files/', blank=True, null=True)

    def __str__(self):
        return self.email


class AllPAgesByAgentControl(models.Model):
    agentEmail=models.CharField(max_length=200)
    firstName = models.CharField(max_length=255)
    email = models.EmailField()
    contactNo = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    pdf_file1 = models.FileField(upload_to='pdf_files/')
    pdf_file2 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file3 = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    pdf_file4 = models.FileField(upload_to='pdf_files/', blank=True, null=True)