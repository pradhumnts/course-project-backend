from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.course),
    path('questions/', views.questions_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)