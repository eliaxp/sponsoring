from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import MedicinesForm
from .models import Medicines
from django.core.urlresolvers import reverse_lazy



class MedicineList(ListView):
    model = Medicines


class MedicineDetail(DetailView):
    model = Medicines


class MedicineCreation(CreateView):
    model = Medicines
    form_class = MedicinesForm
    success_url = reverse_lazy('courses:list')


class CourseUpdate(UpdateView):
    model = Medicines
    success_url = reverse_lazy('courses:list')
    


class CourseDelete(DeleteView):
    model = Medicines
    success_url = reverse_lazy('courses:list')


