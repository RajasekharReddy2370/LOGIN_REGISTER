from django.urls import path
from .views import Home,ALLUSERS,ONEUSER,NEWUSER,UPDATEUSER,DELETEUSER,REGISTER,LOGIN,DASHBOARD

urlpatterns = [
    path('',Home,name = 'homepage'),
    path('au/',ALLUSERS.as_view(),name = "All Users"),
    path('ou/<int:id>/',ONEUSER.as_view(),name = "single User"),
    path('nu/<int:id>/',NEWUSER.as_view(),name = "create new User"),
    path('uu/<int:id>/',UPDATEUSER.as_view(),name = "update existing User"),
    path('du/<int:id>/',DELETEUSER.as_view(),name = "delete existing User"),
    path('du/<int:id>/',DELETEUSER.as_view(),name = "delete existing User"),
    path('reg/',REGISTER.as_view(),name = "Register"),
    path('log/',LOGIN.as_view(),name = "Login"),
    path('db/',DASHBOARD.as_view(),name = "dsb"),
]