from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    

class AvailableTimeForSpecificEngineer(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        engineer_id = request.query_params.get("engineer_id")
        if engineer_id:
            return query_set.filter(engineer = engineer_id)
        return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificEngineer]

class EngineerPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100

class EngineerViewset(viewsets.ModelViewSet):
    queryset = models.Engineer.objects.all()
    serializer_class = serializers.EngineerSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = EngineerPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer