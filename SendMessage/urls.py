from django.urls import path
from SendMessage import views

urlpatterns = [
    path('',views.ReadExcel),
    path('viewexcel/', views.view_excel, name="viewExcel")
]
