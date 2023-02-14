from django.urls import path
from . import views as twoA_views
from . import views

urlpatterns=[
path('delete/', views.delete, name ='delete'),
path('delete/<int:id>', views.delete_data, name ='delete_data'),
	
path('oneA/twoA/', views.twoA, name='twoA'),
path('oneA/twoA/delete/<int:id>', views.delete_data, name ='delete_data'),

path('', views.index, name='index'),



]