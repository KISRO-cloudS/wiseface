from django import forms
from design.models import Report, Comment, Post, Profile
import re





#  f o r m   s y s t e m

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['phone_number','message','company']


# COMMENT

#---------------
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['Help','clip']



# PROFILE
# Create a ProfileUpdateForm to update image

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =['country','birthday','about_me','profile_image','solve_of','age','marital_status',
        'sex','mobile_number','place_of_birth','religion','occupation','street',
        'highest_level_of_education','profession',
        'hobbies','talent','my_slug' ,'follow_me_on',]



# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country','birthday','about_me','profile_image','solve_of','age','marital_status',
        'sex','mobile_number','place_of_birth','religion','occupation','street',
        'highest_level_of_education','profession',
        'hobbies','talent','my_slug' ,'follow_me_on',]




#  POST

class PostForm(forms.ModelForm):


	

	class Meta:
		model = Post
		fields = ['title','problem','A_brief_Discription','clip']

