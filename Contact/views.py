from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_page(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print("Form is valid. Saving data...")
            contact_form.save()  # Save the form data to the database
            return redirect('home_page')  # Redirect after successful submission
        else:
            print("Form is not valid.")
            print(contact_form.errors)
    else:
        contact_form = ContactForm()

    context = {
        'form': contact_form
    }
    return render(request, 'contact/contact.html', context)
