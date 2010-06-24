from django.urls import path
from .views import list_profiles,create_profile,update_profile,delete_profile

urlpatterns = [
    path('', list_profiles, name="list_profiles"),
    path('new/', create_profile, name="create_profile"),
    path('update/<int:id>/',update_profile, name="update_profile"),
    path('delete/<int:id>/', delete_profile,name="delete_profile"),
]
