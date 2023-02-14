from django.db import models
class Good(models.Model):
	A_brief_Discription=models.TextField(max_length=1000,default="Tell Your Condition ...")
	clip=models.FileField(upload_to='videos/%Y/%m/%d/', default='')



	def clip_type_html(self):
		type_tuple = guess_type(self.clip.url, strict=True)
		if (type_tuple[0]).__contains__("image"):
			return "image"
		elif (type_tuple[0]).__contains__("video"):
			return "video"
	


