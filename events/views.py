from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.utils import timezone

from .models import Event


def start(request):
    return render(request, "events/start.html")


def home(request):
    return render(request, "events/home.html")

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'

    def get_queryset(self):
        qs = Event.objects.filter(user = self.request.user).order_by('day')
        return qs

class MonthlyEventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'

    def get_queryset(self):
        qs = Event.objects.filter(user = self.request.user,
                                  day__month = timezone.now().month).order_by('day')
        return qs

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['description', 'day']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].widget = forms.TextInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['description', 'day']
    template_name = 'events/event_edit_form.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].widget = forms.TextInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/home'