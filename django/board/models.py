from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    num = models.AutoField(primary_key=True)
    people = models.IntegerField(null=True)
    title=models.CharField(max_length=100,null=True)
    count = models.IntegerField(null=True)
    main_text = models.TextField(null=True)
    Cdate=models.DateTimeField(default=timezone.now)
    Edate=models.DateTimeField()
    sex=models.BinaryField(null=True)
    create_img=models.ImageField(null=True)
    game=models.TextField(null=True,default="기타")
    location=models.CharField(max_length=100,null=True)
    create_user=models.ForeignKey(User,on_delete=models.CASCADE)
    ALT=models.DecimalField(max_digits=30,decimal_places=20,null=True)
    LAT=models.DecimalField(max_digits=30,decimal_places=20,null=True)
    
    def __str__(self) :
        return str(self.num)
