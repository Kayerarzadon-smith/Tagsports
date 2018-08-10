from __future__ import unicode_literals
from django.db import models
import re

class RequestManager(models.Manager):
    def sample_validator(self, postData):
        NAME_REGEX = re.compile(r'^[A-Za-z ]*$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
        results = {
            'status' : True
        }
        errors = []
        if len(postData['name']) < 2:
            errors.append("Your name is invalid")
        if not re.match(NAME_REGEX, postData['name']):
            errors.append('Name needs letter from the alphabet')
        if len(postData['email']) < 2:
            errors.append('Your email is invalid. Please reenter')
        if not EMAIL_REGEX.match(postData ['email']):
            errors.append('Please sumbit a valid email')
        
        if len (errors) > 0:
            results['status'] = False
            results['errors'] = errors
        else:
            sample = Sample.objects.create(
                name=postData['name'],
                email=postData["email"],
                phone=postData['phone'],
                street=postData['street'],
                city=postData['city'],
                state=postData['state'],
                zipcode=postData['zipcode'],
                organization=postData['organization'],
                sport=postData['sport'],
                colors=postData['colors'],
                helmet=postData['helmet'],
                website=postData['website'],
                instructions=postData['instructions'])
            print sample.name
            print sample.email
            print sample.phone
            print sample.street
            print sample.city
            print sample.state
            print sample.zipcode
            print sample.organization
            print sample.sport
            print sample.colors
            print sample.helmet
            print sample.website
            print sample.instructions
            results['sample'] = sample
        
        return results
    

class Sample(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5)
    organization = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    colors = models.CharField(max_length=255)
    helmet = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RequestManager()
