from django.db import models
from django.conf import settings
# Create your models here.
#from django.contrib.auth.models import User

User=settings.AUTH_USER_MODEL

# class ToDoList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
#     name = models.CharField(max_length=200)

#     def __str__(self):
#     	return self.name


class Todo(models.Model):
	#user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	# todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist")
	content=models.TextField()

	def __str__(self):
		return self.content
