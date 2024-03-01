from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class =  serializers.AppointmentSerializer
    

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        pupil_id = self.request.query_params.get('pupil_id')
        if pupil_id:
            queryset = queryset.filter(pupil_id=pupil_id)
        return queryset