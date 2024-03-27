from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="Student"),
  path("teachers", views.teachers, name="Teachers"),
  path("courses", views.courses, name="Courses"),
]
