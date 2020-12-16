from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='pic')

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.name