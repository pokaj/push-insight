from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, username, email, role, organization, password=None):
        if firstname is None:
            raise TypeError("Users should have firstname")
        if lastname is None:
            raise TypeError("Users should have lastname")
        if username is None:
            raise TypeError("Users should have username")
        if email is None:
            raise TypeError("Users should have email")
        if role is None:
            raise TypeError("Users should have role")
        if organization is None:
            raise TypeError("Users should have organization")

        user = self.model(
            firstname = firstname,
            lastname = lastname,
            username =username,
            email = self.normalize_email(email),
            role = role,
            organization = organization
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, firstname, lastname, username, email, role, organization, password):
        if firstname is None:
            raise TypeError("Users should have firstname")
        if lastname is None:
            raise TypeError("Users should have lastname")
        if username is None:
            raise TypeError("Users should have username")
        if email is None:
            raise TypeError("Users should have email")
        if role is None:
            raise TypeError("Users should have role")
        if organization is None:
            raise TypeError("Users should have organization")
        if password is None:
            raise TypeError("Users should have password")
        
        user = self.create_user(
            firstname = firstname, 
            lastname = lastname, 
            username = username, 
            email = email, 
            role = role, 
            organization = organization
        )
        user.set_password(password)
        user.is_superuser= True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField('First name', max_length=100)
    lastname = models.CharField('Last name', max_length=100)
    username = models.CharField('Username', max_length=100, unique=True)
    email = models.EmailField('E-mail', max_length=100, unique=True)
    ROLE_CHOICES = [('Co', 'Campaign Owner'), ('Ma', 'Manager'), ('Su', 'Supervisor')]
    role = models.CharField('Role', choices=ROLE_CHOICES, max_length=10)
    organization = models.CharField('Organization', max_length=250)
    # initiative = models.CharField('Initiative', max_length=250)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    last_login = models.DateTimeField('last joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'role', 'organization', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }