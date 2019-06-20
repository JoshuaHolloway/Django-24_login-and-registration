from django.db import models

# Create your models here.
class Users(models.Model):
  #id
  first_name = models.CharField(max_length=32)
  last_name = models.CharField(max_length=32)
  email = models.CharField(max_length=64)
  password_hash = models.CharField(max_length=128)
  # logged_in = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Users: ({self.first_name}, {self.last_name}, {self.email})"