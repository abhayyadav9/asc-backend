from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, Instance
from .serializers import CourseSerializer, InstanceSerializer

# Create your views here.

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class InstanceListCreate(generics.ListCreateAPIView):
    serializer_class = InstanceSerializer

    def get_queryset(self):
        queryset = Instance.objects.select_related('course').all()  # Use select_related to optimize the query
        year = self.request.query_params.get('year')
        semester = self.request.query_params.get('semester')
        
        if year:
            queryset = queryset.filter(year=year)
        if semester:
            queryset = queryset.filter(semester=semester)
            
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            # Return the created instance with course details
            return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstanceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Instance.objects.select_related('course').filter(
            year=self.kwargs.get('year'),
            semester=self.kwargs.get('semester')
        )
