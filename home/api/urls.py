# Django imports
from .views import post_List, api_Add , api_Delete
from django.urls import path

urlpatterns = [
    path('post-list/', post_List),
    path('api/', api_Add),
    path('api-delete/', api_Delete),
]
