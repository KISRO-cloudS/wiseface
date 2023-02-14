from django.contrib import admin
from design.models import Notification, Report, About_Us_Page, FollowersCount,Comment,Post,Profile

# a d m i n  s y s t e m 

admin.site.register(Report )


admin.site.register(About_Us_Page)

# PROFILE

admin.site.register(Profile)
admin.site.register(Notification)


# POST

admin.site.register(Post )


# COMMENT

admin.site.register(Comment )


# FOLLOWERCOUNTS

admin.site.register(FollowersCount )



#  e n d  o f  a d m i n  s y s t e m 
