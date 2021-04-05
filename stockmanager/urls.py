from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('addstock/',views.addstock,name="addstock"),
    
    path('delete/<list_id>',views.delete,name="delete")
]
