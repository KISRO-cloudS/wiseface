from django.shortcuts import (render,redirect,get_object_or_404)
from django.http import HttpResponseRedirect
from design.models import Report, About_Us_Page, FollowersCount, Comment,Post,User,Profile
from design.forms import ReportForm, CommentForm,PostForm,ProfileForm,ProfileUpdateForm
from django.utils import timezone
from django.views import generic
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import itertools
from django.db.models import Q
import json
from django.db import transaction
from django.core.paginator import Paginator

from django.views.generic import TemplateView, ListView, DetailView
from itertools import chain


def chat (request):
	return render(request,'chat/chat.html',{})



class ChatListView(ListView):
	model = Profile
	template_name = 'chat/chat.html'
	context_object_name = 'profiles'

	def get_queryset(self):
		return Profile.objects.all().exclude(user=self.request.user)


class ChatDetailView(DetailView):
	model = Profile
	template_name = 'chat/chat2.html'

	def get_object(self, **kwargs):
		pk = self.kwargs.get('pk')
		view_profile = Profile.objects.get(pk=pk)
		return view_profile

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		view_profile= self.get_object()
		my_profile = Profile.objects.get(user=self.request.user)
		if view_profile.user in my_profile.following.all():
			follow = True
		else:
			follow = False
		context["follow"]=follow
		return context



	
