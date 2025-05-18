from django.urls import path
from . import views

urlpatterns = [
  path('doctors/', views.DoctorListView.as_view(), name='doctors_list'),
  path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
  
  path('appointments/new/', views.AppointmentCreateView.as_view(), name='appointment-create'),
  path('appointments/', views.AppointmentListView.as_view(), name='appointment-list'),
  path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),

]