from rest_framework import serializers
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    pupil = serializers.StringRelatedField(many=False)
    engineer = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Appointment
        fields = '__all__'
