from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['engineer_name', 'pupil_name', 'appointment_types', 'appointment_status', 'problemstat', 'time', 'cancel']
    def pupil_name(self,obj):
        return obj.pupil.user.first_name
    
    def engineer_name(self,obj):
        return obj.engineer.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.pupil.user, 'engineer' : obj.engineer})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.pupil.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
    
admin.site.register(models.Appointment, AppointmentAdmin)