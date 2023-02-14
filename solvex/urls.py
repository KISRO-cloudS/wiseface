"""solvex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from accounts import views as user_views
from accounts.views import logout

from django.views.generic import TemplateView

from chat.views import (chat, 
    ChatListView,
    ChatDetailView,)

from payments.views import (Pay,
payment_completed,
payment_failed 
)



from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


from design.views import (



#  U R L 
index,  
profile,

Search,
zeroA,

postform,



like,

likepost,

postdetail,

postlist,

comment,

commentpost,

solution,

solutionpost,

twoA,

userp,



prof_edit,


usage,
terms_and_conditions,
about_us,
reportform,
landing_page,
Searchprofile,
ShowNotifications,
DeleteNotifications,
following,
followers,
ProfileListView,
ProfileDetailView,
follow_unfollow_profile,

	)

urlpatterns = [
    path('admin/', admin.site.urls),

     path('pay/', Pay, name='pay'),

     path('payment_completed/', payment_completed, name='payment-completed'),
     path('payment_failed/', payment_failed, name='payment-failed'),


    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
  path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path('password-reset-email/', PasswordResetView.as_view(html_email_template_name='accounts/password_reset_email.html'),name='password-reset'),



    path('logout/',logout,name='logout'),
    path('account/', include('allauth.urls')),

    path('searchprofile/',Searchprofile,name='searchprofile'),

    path('chat/', chat, name='chat'),
    path('notification/',ShowNotifications , name='notification'),
    path('notification/<noti_id>/delete',DeleteNotifications , name='del-notification'),

       path('chats/', ChatListView.as_view(), name='chat-list-view'),

    path('chats/<pk>/', ChatDetailView.as_view(), name='chat-detail-view'),
  
 path('search/',Search,name='search'),

     path('following/', following, name='following'),
      path('followers/', followers, name='followers'),

    path('userp/<str:username>/', userp, name='userp'),

    path('/', index, name='index'),

        path('profilez/', ProfileListView.as_view(), name='profile-list-view'),

    path('profilez/<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),

    path('switch_follow/', follow_unfollow_profile, name='follow-unfollow-view'),



    path('about_us/', about_us, name='about_us'),
    path('terms/', terms_and_conditions, name='terms_and_conditions'),
    path('usage/',usage , name='usage'),

    path('landing_page/',landing_page, name='landing_page'),

    path('profile/', profile, name='profile'),

    path('postform/', postform, name='postform'),




    path('like/<int:pk>/', likepost, name='likepost'),

    path('postlist/like/<int:pk>/', like, name='like'),

    path('comment/<int:pk>', comment, name='comment'),

    path('postlist/comment/<int:pk>/', commentpost, name='commentpost'),
 
    path('postlist/', postlist, name='postlist'),

    path('solution/<int:pk>', solutionpost, name='solutionpost'),

    path('oneA/twoA/solution/<int:pk>',solution,name='solution'),

    path('postdetail/', postdetail, name='postdetail'),

    path('zeroA/',zeroA,name='zeroA'),
    path('reportform/',reportform,name='reportform'),

    path('prof_edit/',prof_edit,name='prof_edit'),

    path('', include('design.urls')),

    path('oneA/twoA/<int:pk>/<int:user>/',twoA, name='twoA'),

 
     
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)