from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'date_submitted')
    search_fields = ('full_name', 'email', 'subject')
