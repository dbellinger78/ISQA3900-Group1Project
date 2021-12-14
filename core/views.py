from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def about(request):

    return render(request, 'templatepage.html',{})
def contact(request):
    if request.method == "POST":
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['testermaverick21@gmail.com'])
        return HttpResponse('Thank you for submitting the form, we will be touch soon')
    return render(request, 'contact.html', {})