from django.db import models

# Create your models here.
class Profile(models.Model):
      uid = models.IntegerField(default=0)
      isCompany = models.IntegerField(default=0)
      firstname = models.CharField(max_length=250)
      lastname = models.CharField(max_length=250)
      email = models.CharField(max_length=250)
      phone = models.CharField(max_length=250)
      city = models.IntegerField(default=0)
      state = models.IntegerField(default=0)
      country = models.IntegerField(default=0)
      status = models.IntegerField(default=0)
      createdate = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.description



