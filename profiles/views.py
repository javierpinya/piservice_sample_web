from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Profile

# Create your views here.

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(TemplateView):
	template_name = 'profiles/profile_form.html'
	success_url = reverse_lazy('profiles')

	def get_object(self):
		# recuperar el objeto que se va a editar
		profile, created = Profile.objects.get_or_create(user=self.request.user)
		return profile

class ProfileListView(ListView):
	model = Profile
	template_name = 'profiles/profile_list.html'

@method_decorator(login_required,name='dispatch')
class ProfileDetailView(DetailView):
	model = Profile

@method_decorator(login_required,name='dispatch')
class ProfileDeleteView(DeleteView):
	model = Profile
	success_url = reverse_lazy('profiles:profiles')