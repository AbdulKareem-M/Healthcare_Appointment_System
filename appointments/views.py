from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Doctor, Appointment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class DoctorListView(ListView):
  model = Doctor
  template_name = 'doctors.html'
  context_object_name = 'doctors'
  
class DoctorDetailView(DetailView):
  model = Doctor
  template_name = 'doctor_detail.html'
  context_object_name = 'doctor'

# appointment views

class AppointmentCreateView(LoginRequiredMixin, CreateView):
  model = Appointment
  template_name = 'appointments/appointment_form.html'
  fields = ['doctor','date','time','reason']
  success_url = reverse_lazy('appointment-list')
  
  def form_valid(self, form):
    form.instance.patient = self.request.user  # set the logged-in user as patient
    return super().form_valid(form)

class AppointmentListView(LoginRequiredMixin, ListView):
  model = Appointment
  template_name = 'appointments/appointment_list.html'
  context_object_name = 'appointments'
  ordering = ['date','time']


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
  model = Appointment
  template_name = 'appointments/appointment_confirm_delete.html'
  success_url = reverse_lazy('appointment-list')