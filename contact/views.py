from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        
        message = """
        
        New message: {}
        
        Name: {}
        
        Subject: {}
        
        FROM: {}
        
        """.format(data['message'], data['name'], data['subject'], data['email'])
        
        send_mail(data['subject'], message, '', ['omer.osmanov11@gmail.com'])
        
    return render(request, 'index.html', {})