from django.urls import path
from .views import list_usertypes,create_usertype,update_usertype,delete_usertype

urlpatterns = [
    path('', list_usertypes, name="list_usertypes"),
    path('new/', create_usertype, name="create_usertype"),
    path('update/<int:id>/',update_usertype, name="update_usertype"),
    path('delete/<int:id>/', delete_usertype,name="delete_usertype"),
]