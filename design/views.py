from django.shortcuts import (render,redirect,get_object_or_404)
from django.http import HttpResponseRedirect
from design.models import Notification, Report, About_Us_Page, FollowersCount, Comment,Post,User,Profile
from design.forms import ReportForm, CommentForm,PostForm,ProfileForm,ProfileUpdateForm
from django.utils import timezone
from accounts.forms import UserUpdateForm
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


def follow_unfollow_profile(request):
	if request.method=="POST":
		my_profile = Profile.objects.get(user=request.user)
		pk = request.POST.get('profile_pk')
		obj = Profile.objects.get(pk=pk)
		if obj.user in my_profile.following.all():
			my_profile.following.remove(obj.user)
		else:
			my_profile.following.add(obj.user)

		return redirect(request.META.get('HTTP_REFERER'))
	return redirect('profile-list-view')


class ProfileListView(ListView):
	model = Profile
	template_name = 'design/main.html'
	context_object_name = 'profiles'

	def get_queryset(self):
		return Profile.objects.all().exclude(user=self.request.user)


class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'design/detail.html'

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





def following(request):
	profile = Profile.objects.get(user=request.user)
	
	return render(request,'design/following.html',{'profile':profile})

def followers(request):
	profile = Profile.objects.get(user=request.user)
	
	return render(request,'design/followers.html',{'profile':profile})



def ShowNotifications(request):
	user = request.user
	notifications = Notification.objects.filter(user=user).order_by('-date')
	Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

	context={
	'notifications':notifications
	}
	return render(request,'design/notifications.html',context)



def DeleteNotifications(request,noti_id):
	user = request.user
	Notification.objects.filter(id=noti_id, user=user).delete()
	return redirect('notification')



def CountNotifications(request):
	count_notifications = None
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()
	return {'count_notifications': count_notifications}















def Searchprofile(request):
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			var = Profile.objects.filter(country__contains = query)
			return render(request,'design/searchprofile.html',{'var':var})
		else:
			print('No information to show')
			return render(request,'design/searchprofile.html',{})





def Search(request):
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			var = Post.objects.filter(title__contains = query)
			return render(request,'design/searchbar.html',{'var':var})
		else:
			print('No information to show')
			return render(request,'design/searchbar.html',{})












def index(request):
	return render(request,'design/index.html',{})
	

def landing_page(request):
	return render(request,'design/landing.html',{})


@login_required

def reportform(request):
	if request.method == 'POST':
		form = ReportForm(request.POST, request.FILES)
		if form.is_valid():
			post	=	form.save(commit=False)
	
			post.user = request.user
			post.created_on=timezone.now()
			post.save()

			return HttpResponseRedirect('/zeroA')
	else:
		form = ReportForm()
	return render(request,'design/reportform.html', {'form': form})






def usage(request):
	return render(request,'design/usage.html',{})


def terms_and_conditions(request):
	return render(request,'design/terms.html',{})


def about_us(request):
	b = About_Us_Page.objects.filter()
	
	return render(request,'design/aboutus.html',{'b':b})


#CART



# PROFILE EDITING
@login_required
def prof_edit(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'design/prof_edit.html', context)	

# SEARCHING ENGINE
class SearchView(TemplateView):
	template_name = 'design/postlist.html'
class SearchsView(ListView):
	model = User
	template_name = 'design/search.html'
	def get_queryset(self):
		query = self.request.GET.get("q")
		object_list = User.objects.filter(Q(name__icontains=query)|Q(state_icontains=query))
		return object_list
		


# HELP SYSTEM
@login_required
def comments(request):
	comments = Comment.objects.order_by('-created_on')
	comments.user = request.user
	return render(request,'design/comments.html',{'comments':comments})



# SOLUTION SYSTEM
@login_required
def solutionpost (request, pk):

	post =Comment.objects.get(pk=pk)
	context={
	'post':post
	}

	return render(request,'design/solution.html',context)


@login_required
def solution(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments=Comment.objects.filter(post=post)
	if request.method =='POST':
		comment_form = CommentForm(request.POST, request.FILES)
		if comment_form.is_valid():
			comment=comment_form.save(commit=False)
			comment.post = post
			comment.user= request.user
			comment.created_on=timezone.now()
			comment.save()	
		url = reverse('solution', args=[str(pk)])
		return redirect(url)	
	else:
		comment_form=CommentForm()

	return render(request,'design/solution.html', {'comment_form':comment_form, 'comments':comments, 'post':post})











# HELP SYSTEM 2
@login_required
def commentpost (request, pk):

	post =Comment.objects.get(pk=pk)
	context={
	'post':post
	}

	return render(request,'design/comment.html',context)


@login_required
def comment(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments=Comment.objects.filter(post=post, user= request.user)
	if request.method =='POST':
		comment_form = CommentForm(request.POST, request.FILES)
		if comment_form.is_valid():
			comment=comment_form.save(commit=False)
			comment.post = post
			comment.user= request.user
			comment.created_on=timezone.now()
			comment.save()		
		url = reverse('comment', args=[str(pk)])
		return redirect(url)	
	else:
		comment_form=CommentForm()

	return render(request,'design/comment.html', {'comment_form':comment_form, 'comments':comments, 'post':post})





# USER FOLLOWING / FOLLOWER SYSTEM
@login_required
def userp(request, username):
	current_user= User.objects.get(username=username)
	logged_user =User.objects.get(username=request.user.username)
	user_follower = len(FollowersCount.objects.filter(user=current_user) )
	user_following = len(FollowersCount.objects.filter(follower=current_user) )
	user_followin = FollowersCount.objects.filter(follower=current_user)
	user_followerx = FollowersCount.objects.filter(user=current_user)
	user_profile = Profile.objects.filter(user=current_user)
	user_follower0 = FollowersCount.objects.filter(user=current_user)
	var = Post.objects.filter(author=current_user)
	

	return render(request,'design/userp.html',{	'current_user':current_user,
		'user_follower':user_follower,
		'user_following':user_following,
		'user_profile':user_profile,
		
		'var':var,
		
	
		
		})


	
	

# SORRY SYSTEM
@login_required
def likepost (request, pk):

	post =Post.objects.get(pk=pk)
	context={
	'post':post
	}

	return render(request,'design/like.html',context)

@login_required
def like(request, pk):


    if request.method == "POST":

        #make sure user can't like the post more than once. 
             user = User.objects.get(username=request.user.username)
        #find whatever post is associated with like
             post = Post.objects.get(pk=pk)
             post.user_likes.add(user)
             post.save()
    url = reverse('likepost', args=[str(pk)])
    return redirect(url)

    


# USER SOLUTIONS FOR PROBLEM
@login_required
def twoA(request):
	var =Post.objects.filter(author=request.user)
	
	return render(request,'design/twoA.html',{'var':var} )	


# POSTS SYSTEM

@login_required
def postdetail(request):
	post = get_object_or_404(Post )
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('threeA')
	else:
		form =CommentForm()

	
	return render(request,'design/postdetail.html', {'form':form, 'var':var})



@login_required
def postlist(request):
	# get the logged in user profile
	profile = Profile.objects.get(user=request.user)
	# check who we are following
	users = [user for user in profile.following.all()]
	# initial values for valiables
	var = []
	qs = None
	# get the post of people we are following
	for u in users:
		p = Profile.objects.get(user=u)
		b = p.user.poster.all()
		var.append(b)
	# our posts
	v = profile.profile_posts()
	var.append(v)
	
	# sort and chain querysets and unpack the posts list
	if len(var)>0:
		qs = sorted(chain(*var), reverse=True, key=lambda obj: obj.created_on)

	return render(request,'design/postlist.html', {'profile':profile, 'var':qs})



@login_required

def postform(request):
	p = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():

			instance	=	form.save(commit=False)
			
			instance.author = request.user
			instance.created_on=timezone.now()
			instance.save()

			return HttpResponseRedirect('/oneA/twoA')
	else:
		form = PostForm()
	return render(request,'design/postform.html', {'form': form})








# PROFILE Update 
@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'design/profile.html', context)


# DELETING OBJECTS

@login_required
def delete (request):
	return render(request,'design/delete.html',{})
	
@login_required
def delete_data(request, id):
    dash_id = int(id)
    try:
        dash_sel = Dashboard.objects.get(id = id)
    except Dashboard.DoesNotExist:
        return redirect('/delete')
    dash_sel.delete()
    return redirect('/delete')
	

# SUCCESS PAGE
@login_required
def zeroA(request):
	return render(request,'design/zeroA.html',{})


#
#	user_follower0 = FollowersCount.objects.filter(user=current_user)
	
#	user_follower1 = []
#	for i in user_follower0:
#		user_follower0 = i.follower
#		user_follower1.append(user_follower0)

#	if logged_user in user_follower1:
#		follow_button_value = 'unfollow'
#	else:
#		follow_button_value = 'follow'