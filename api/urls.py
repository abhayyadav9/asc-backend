from django.urls import path
from .views import (
    CourseListCreate,
    CourseRetrieveUpdateDestroy,
    InstanceListCreate,
    InstanceRetrieveUpdateDestroy
)

urlpatterns = [
    path('courses', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>', CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve-update-destroy'),
    path('instances', InstanceListCreate.as_view(), name='instance-list-create'), # For POST to create instance
    path('instances/<int:year>/<int:semester>', InstanceListCreate.as_view(), name='instance-list-year-semester'), # For GET to list instances
    path('instances/<int:year>/<int:semester>/<int:id>', InstanceRetrieveUpdateDestroy.as_view(), name='instance-retrieve-update-destroy'),
] 