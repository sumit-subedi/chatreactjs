from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
class message(models.Model):
	message = models.TextField()
	sent = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)

	def __str__(self):
		return str(self.message[:6])
