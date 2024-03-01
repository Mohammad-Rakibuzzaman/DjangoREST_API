from django.db import models
from pupil.models import Pupil
from sengineer.models import Engineer, AvailableTime
# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
APPOINTMENT_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class Appointment(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete = models.CASCADE)
    engineer = models.ForeignKey(Engineer, on_delete = models.CASCADE)
    appointment_types = models.CharField(choices = APPOINTMENT_TYPES, max_length = 10)
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS, max_length = 10, default = "Pending")
    problemstat = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Engineer: {self.engineer.user.first_name} , Pupil : {self.pupil.user.first_name}"
    