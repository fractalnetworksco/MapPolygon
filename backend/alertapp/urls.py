from django.urls import path
from . import views
urlpatterns=[
    path('addAlert/',views.AddAlert),
    path('allAlert/',views.GetAllAlert),
    path('test/',views.test),
    path('resolveAlert/<alertId>/',views.ResolveAlert),
    path('sendMessage/<alertId>/',views.SendMessage),
    ]
