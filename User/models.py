from django.db import models

# Create your models here.
class User(models.Model):
      username = models.CharField(max_length=50)
      password = models.CharField(max_length=255)
      secret = models.CharField(max_length=255)
      isemailverified = models.IntegerField(default=0)
      isphoneverified  = models.IntegerField(default=0)
      status = models.IntegerField(default=0)
      createdate = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.description





