from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Profile
from .forms import ProfileForm,ProfileUpdateForm

# Create your views here.

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
	model = Profile
	form_class = ProfileUpdateForm
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse_lazy('vehiculos:update_profile', args=[self.object.id]) + '?ok'

@method_decorator(login_required,name='dispatch')
class ProfileListView(ListView):
	model = Profile
	#template_name = 'profiles/profile_list.html'

@method_decorator(login_required,name='dispatch')
class ProfileDetailView(DetailView):
	model = Profile
	#form_class = ProfileForm
	template_name = 'profiles/profile_detail.html'
	#success_url = reverse_lazy('profiles:profile')

	def get_success_url(self):
		return reverse_lazy('profiles:update_profile', args=[self.object.id])

@method_decorator(login_required,name='dispatch')
class ProfileDeleteView(DeleteView):
	model = Profile
	success_url = reverse_lazy('profiles:profiles')