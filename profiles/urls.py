from django.urls import path
from .views import ProfileUpdate,ProfileListView,ProfileDetailView,ProfileDeleteView

profiles_patterns = ([
	path('',ProfileListView.as_view(),name='profiles'),
	path('<int:pk>/<slug:slug>',ProfileDetailView.as_view(),name='detail_profile'),
	path('profile/',ProfileUpdate.as_view(),name='profile'),
	path('update/<int:pk>', ProfileUpdate.as_view(), name='update_profile'),
	path('delete/<int:pk>', ProfileDeleteView.as_view(), name='delete_profile'),
], 'profiles')