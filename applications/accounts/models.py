from django.db import models
from .managers import UserAdminCreationForm
from django.contrib.auth.models import AbstractBaseUser


#  Class || Custom User Model
class User(AbstractBaseUser):

    # DJANGO || Django required fields to overwrite default Django User Model
    email           = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    # CUSTOM || Custom fields to add to custom User Model
    firstname = models.CharField(max_length=30)

    # DJANGO || Required field to tell Django which field use to connect user
    USERNAME_FIELD = 'username'

    # DJANGO || Required fields during user registration | No need to mention USERNAME_FIELD
    REQUIRED_FIELDS = ['email', 'firstname']

    # DJANGO || Specify Custom Managing Class
    objects = UserAdminCreationForm()

    def __str__(self):
        return self.firstname

    # DJANGO || Give permissions access to Admin user
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # DJANGO || Give user access to permission modules
    def has_module_perms(self, app_label):
        return True
