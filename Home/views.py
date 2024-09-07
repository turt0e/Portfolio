from django.shortcuts import render
from Contact.models import Contact

def home_page(request):
    inquiries = Contact.objects.all()
    return render(request, 'home.html', {'inquiries': inquiries})

