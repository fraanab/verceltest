from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Notes(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	text = models.TextField(max_length = 255)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'User: {self.username}, note: {self.text}'
