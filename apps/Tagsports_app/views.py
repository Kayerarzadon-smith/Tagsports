from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index (request):
    return render(request, "Tagsports_app/landing.html")

def process (request):
    results = Sample.objects.sample_validator(request.POST)
    if (results['status']):
        request.session['errors'] = []
        request.session['name'] = results['sample'].name
        request.session['email'] = results['sample'].email
        request.session['phone'] = results['sample'].phone
        request.session['street'] = results['sample'].street
        request.session['city'] = results['sample'].city
        request.session['state'] = results['sample'].state
        request.session['zipcode'] = results['sample'].zipcode
        request.session['organization'] = results['sample'].organization
        request.session['sport'] = results['sample'].sport
        request.session['colors'] = results['sample'].colors
        request.session['helmet'] = results['sample'].helmet
        request.session['website'] = results['sample'].website
        request.session['instructions'] = results['sample'].instructions
        request.session['sample_id'] = results['sample'].id
        print "CHECKPOINT: You have successfully submitted a sample request!"
        return redirect('/results')
    else: 
        for error in results ['errors']:
            messages.error(request, error)
            print "ERROR MESSAGE: Sorry, you need to register again"
        return redirect ('/') 


    # print "CHECKPOINT: POST NAME has been recognized."
    # request.session['email'] = request.POST['email']
    # print "CHECKPOINT: POST EMAIL has been recognized."
    # request.session['phone'] = request.POST['phone']
    # print "CHECKPOINT: POST PHONE has been recognized."
    # request.session['street'] = request.POST['street']
    # print "CHECKPOINT: POST STREET has been recognized."
    # request.session['city'] = request.POST['city']
    # print "CHECKPOINT: POST CITY has been recognized."
    # request.session['state'] = request.POST['state']
    # print "CHECKPOINT: POST STATE has been recognized."
    # request.session['zip'] = request.POST['zip']
    # print "CHECKPOINT: POST ZIP has been recognized."
    # request.session['org'] = request.POST['org']
    # print "CHECKPOINT: POST ORG has been recognized."
    # request.session['sport'] = request.POST['sport']
    # print "CHECKPOINT: POST SPORT has been recognized."
    # request.session['colors'] = request.POST['colors']
    # print "CHECKPOINT: POST COLORS has been recognized."
    # request.session['helmet'] = request.POST['helmet']
    # print "CHECKPOINT: POST HELMET has been recognized."
    # request.session['website'] = request.POST['website']
    # print "CHECKPOINT: POST WEBSITE has been recognized."
    # request.session['website'] = request.POST['website']
    # print "CHECKPOINT: POST WEBSITE has been recognized."
    # request.session['desc'] = request.POST['desc']
    # print "CHECKPOINT: POST SPECIAL INSTRUCTIONS has been recognized."
    # if len(request.POST['name']) < 2:
    #  print "ERROR MESSAGE: Your name is invalid. You're now being redirected to localhost:8000 to enter a valid name."
    # if len(request.POST['email']) < 2:
    #     print "ERROR MESSAGE: Your email is invalid. You're now being redirected to localhost:8000 to enter a valid email."
    #     return redirect('/')
    # else:
    #     print 'CHECKPOINT: You are now being redirected to localhost:8000/results'

def results(request):
    print 'CHECKPOINT: You are now being redirected to localhost:8000/results'
    return render(request, 'Tagsports_app/results.html')

def back(request):
    return redirect('/')
