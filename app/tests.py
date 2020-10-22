# from django.test import TestCase

# from .serializers import RegisterSerializer, LoginSerializer
# from django.contrib.auth.models import User
# from django.urls import reverse, resolve
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.test import TransactionTestCase, Client

import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import RegisterSerializer
from django.test import TransactionTestCase, Client

from django.contrib.auth import get_user_model

# making reference to custom user model
User = get_user_model()


class ValidUserLoginTestCase(APITestCase):

    '''
    This test is to assert for a valid login sinario
    To do so a new user registration test case will 
    be created, after which the successfully created
    new user will be used to test the login endpoint
    for a valid login sinario    
    '''

    # A new user is singned up
    def test_register_new_user(self):
        userdata = {

            "firstname": "Moses",
            "lastname": "wuniche",
            "username": "moseswuniche",
            "email": "moses@gmail.com",
            "organization": "Misty Inc",
            "role": "Ma",
            "password": "moses123",

        }

        response = self.client.post("/api/register/", userdata)
        self.assertEqual(response.status_code, 200)

        # create and save user for testing
    def setUp(self):
        # User.objects.get()
        # creating temp user to use for testing
        user = User.objects.create(
            firstname="Moses",
            lastname="wuniche",
            username="mosesalhassan",
            email="wuniche@gmail.com",
            organization="Misty Inc",
            role="Ma",
            password="moses123",
        )
        user.set_password("moses123")
        user.save()

        # test registred user valid login
    def test_valid_login(self):
        print("got here")
        newuser = Client()
        response = newuser.login(
            email="wuniche@gmail.com", password="moses123")
        self.assertTrue(response)
