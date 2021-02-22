from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    #return HttpResponse("Hello everyone")
    if request.method == 'POST':
        def_name = request.POST['name']
        def_email = request.POST['email']
        def_subject = request.POST['subject']
        def_msg = request.POST['message']
        user = Contact(
            user_name = def_name,
            user_email = def_email,
            user_subject=def_subject,
            user_msg=def_msg
            )
    
        user.save()
        return HttpResponse("Your message has been sent. Thank you!!!")
    
    return render(request, "index.html")