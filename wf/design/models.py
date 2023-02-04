
from django.db import models

import datetime
from	django.utils	import	timezone

from django.contrib.auth.models import User, Group, Permission
  
from PIL import Image

from mimetypes import guess_type
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ckeditor.fields import RichTextField







#  m o d e l  s y s t e m


sex = (
	('Male','Male'),
	('Female','Female'),
	
	
	)


marital_status = (
	('Married','Married'),
	('Single','Single'),
	('Divorced','Divorced'),
	('Widowed','Widowed'),
	('Separated','Separated'),
	
	)


#Post

solve = (
		('academic problems','academic problems'),
		('agricultural problems','agricultural problems'),
		('adventure problems','adventure problems'),
		('anxiety problems','anxiety problems'),
		('business problems','business problems'),
		('biological problems','biological problems'),
		('chemical problems','chemical problems'),
		('ceremonic problems','ceremonic problems'),
		('confidential problems','confidential problems'),
		('climentic problems','climentic problems'),
		('depression problems','depression problems'),
		('developmental problems','developmental problems'),
		('boredom problems','boredom problems'),
		('emotional problems','emotional problems'),
		('environmental problems','environmental problems'),
		('fashion and design problems','fashion and design problems'),
		('financial problems','financial problems'),
		('friendship problems','friendship problems'),
		('freedom problems','freedom problems'),
		('health problems','health problems'),
		('love and relationship problems','love and relationship problems'),
		('medical problems','medical problems'),
		('mental problems','mental problems'),
		('parental problems','parental problems'),
		('political problems','political problems'),
		('religious problems','religious problems'),
		('research and discovery problems','research and discovery problems'),
		('stress problems','stress problems'),
		('shopping problems','shopping problems'),
		('security problems','security problems'),
		('self defence problems','self defence problems'),
		('Self esteem problems','Self esteem problems'),
		('self care problems','self care problems'),
		('self control problems','self control problems'),
		('sports problems','sports problems'),
		('talental problems','talental problems'),
		('technological problems','technological problems'),
		('traditional problems','traditional problems'),
		('travel problems','travel problems'),
		('Other problems','Other problems'),
		


		)

class Report(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(default='+', max_length=15)
	message = models.TextField(max_length=10000, default='tell us something..') 
	company = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=timezone.now)





class About_Us_Page(models.Model):
	main_description = models.TextField(max_length=1000, default='about our app')
	service_title = models.CharField(max_length=100, default='service_name')
	service_description = models.TextField(max_length=300, default='about our service')
	service_title2 = models.CharField(max_length=100, default='service_name')
	service_description2 = models.TextField(max_length=300, default='about our service')
	service_title3 = models.CharField(max_length=100, default='service_name')
	service_description3 = models.TextField(max_length=300, default='about our service')
	team_member_name1 = models.CharField(max_length=70, default='name')
	team_member_role1 = models.CharField(max_length=100, default='role')
	team_member_image1 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')
	team_member_name2 = models.CharField(max_length=70, default='name')
	team_member_role2 = models.CharField(max_length=100, default='role')
	team_member_image2 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')
	team_member_name3 = models.CharField(max_length=70, default='name')
	team_member_role3 = models.CharField(max_length=100, default='role')
	team_member_image3 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')
	team_member_name4 = models.CharField(max_length=70, default='name')
	team_member_role4 = models.CharField(max_length=100, default='role')
	team_member_image4 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')





























class Notification(models.Model):
	NOTIFICATION_TYPE = (
		(1, ('Comment')),
		 )

	post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='noti_post',blank=True, null=True, default='')
	sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='noti_from_user')
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='noti_to_user')
	notification_type = models.IntegerField(default=1)
	text_preview = models.CharField(max_length=50, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)
	notification_type = models.PositiveSmallIntegerField(choices=NOTIFICATION_TYPE)
    






# FOLLOWING AND FOLLOWERS







#  FOR PROFILE

class Profile(models.Model):
    solve_of = models.CharField(default='',max_length=1000,choices=solve)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_image=models.ImageField(upload_to='profile_pics', default='profile_pics/lo.png')
    my_slug = models.CharField(  max_length=20, default='my slug')
    following = models.ManyToManyField(User, blank=True, related_name= "following", symmetrical=False)
    follow_me_on = models.TextField(max_length=300, default='www.other_sites.com')
    sex = models.CharField(default='',max_length=1000,choices=sex)
    marital_status = models.CharField(default='',max_length=1000,choices=marital_status)
    talent = models.CharField(max_length=100, default='None')
    street = models.CharField(max_length=100, default='None')
    place_of_birth = models.CharField(max_length=100, default='None')
    country = models.CharField(max_length=100, default='None')
    hobbies = models.CharField(max_length=100, default='None')
    highest_level_of_education = models.CharField(max_length=100, default='None')
    profession = models.CharField(max_length=100, default='None')
    mobile_number = models.CharField(max_length=100, default='None')
    religion = models.CharField(max_length=100, default='None')
    occupation = models.CharField(max_length=100, default='None')
    age = models.PositiveIntegerField(default=0)
    created_on= models.DateTimeField(default=timezone.now)
    about_me = models.TextField(max_length=200, default='about_me')
    birthday =models.CharField(default='1/1/1999',max_length=10)
    
 
    def __str__(self):
         return f'{self.user.username} Profile'

    def profile_posts(self):
    	return self.user.poster.all()

    class Meta:
    	ordering = ('-created_on',)





    def save(self, *args, **kwargs):
    	super(Profile, self).save(*args, **kwargs)
    	img = Image.open(self.profile_image.path)
    	if img.height > 300 or img.width > 300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.profile_image.path)
    	 # Open image


    

    	


        
        
        # resize image
        
            
             # Resize image
            

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# like signals









# POST

class Post(models.Model):
	author	=	models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
	problem = models.CharField(default='', max_length=1000,choices=solve)
	A_brief_Discription=RichTextField(blank=True, null=True)

	#A_brief_Discription=models.TextField(max_length=1000,default="Tell Your Condition ...")
	clip=models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	user_likes = models.ManyToManyField(User)
	created_on = models.DateTimeField(default=timezone.now)
	likes = models.PositiveIntegerField(default=0)
	title = models.CharField(max_length=200, default='title')

	def __str__(self):
		return str(self.A_brief_Discription)[:30]

	
	def total_likes(self):
		return self.user_likes.count()



	class Meta:
		ordering =['-created_on']	
    




	def clip_type_html(self):
		type_tuple = guess_type(self.clip.url, strict=True)
		if (type_tuple[0]).__contains__("image"):
			return "image"
		elif (type_tuple[0]).__contains__("video"):
			return "video"






class FollowersCount(models.Model):
	follower = models.CharField(max_length=1000)
	user =models.CharField(max_length=1000)

	def __str__(self):
         return self.user



# COMMENT

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	Help = RichTextField(blank=True, null=True)
	clip=models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	created_on = models.DateTimeField(default=timezone.now)
	


	def user_comment_post(sender, instance, *args, **kwargs):
		comment = instance
		post = comment.post
		sender = comment.user
		text_preview = comment.Help[:50]
		notify = Notification(post=post, sender=sender, user = post.author, text_preview=text_preview, notification_type=1)
		notify.save()

	def user_del_comment_post(sender, instance, *args, **kwargs):
		comment = instance
		post = comment.post
		sender = comment.user
		text_preview = comment.body[:50]
		notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
		notify.delete()

	def clip_type_html(self):
		type_tuple = guess_type(self.clip.url, strict=True)
		if (type_tuple[0]).__contains__("image"):
			return "image"
		elif (type_tuple[0]).__contains__("video"):
			return "video"	

	class Meta:
		ordering =['-created_on']









post_save.connect(Comment.user_comment_post,sender=Comment)
post_delete.connect(Comment.user_del_comment_post,sender=Comment)