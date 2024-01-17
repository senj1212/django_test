from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexPage.as_view()),
    path('get_employees_by_manager_id', get_employees_by_manager_id)
]