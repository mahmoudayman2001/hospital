from django.shortcuts import  render, redirect, reverse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView , CreateView , UpdateView , DeleteView, DetailView)
from .models import Appoinment , Doctor , Patient
from .forms import DoctorForm , AppoinmentForm
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin



def signup (request):
    form = SignupForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        user = form.save()
        login(request , user)
        return redirect('Appoinment-create')
    
    return render(request , 'signup.html' , {'form':form})


class DoctorCreateView(UserPassesTestMixin, CreateView) :
    form_class = DoctorForm
    template_name = "Doctor_form.html"
    def test_func(self):
        return self.request.user.is_staff


class Doctorslistview(ListView):
    model = Doctor
    template_name = "index.html" 
    login_url = reverse_lazy('login')
    

class AppointmentCreateView(CreateView):
    model = Appoinment
    form_class = AppoinmentForm
    template_name = "Appoinment_form.html"
    success_url = reverse_lazy("Appoinment-create")

    def form_valid(self, form):
        # Check if the appointment conflicts with existing appointments
        existing_appointments = Appoinment.objects.filter(
            doctor=form.cleaned_data['doctor'],
            date=form.cleaned_data['date'],
            time=form.cleaned_data['time'],
            booked=True
        )
        if existing_appointments.exists():
            # If an existing appointment exists, return an error message
            form.add_error(None, 'This appointment has already been booked. Please choose another time slot.')
            return super().form_invalid(form)
        
        # If no existing appointments, create a new appointment
        form.instance.booked = True
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     form.add_error(None, "You can't book an appointment at this time.")
    #     return super().form_invalid(form)
    

class Appoinmentlistview(UserPassesTestMixin, ListView):
    model = Appoinment
    template_name = "Appoinment_list.html" 
    def test_func(self):
        return self.request.user.is_staff  



class DoctorDetailView(UserPassesTestMixin, DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = self.get_object()
        appointments = Appoinment.objects.filter(doctor=doctor)
        context['appointments'] = appointments
        return context




