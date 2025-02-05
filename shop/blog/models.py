from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    class STATUS(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published' 
        REJECTED = 'RJ', 'Rejected'

    author = models.ForeignKey(User,on_delete= models.CASCADE)
    title = models.CharField(max_length=250,null=False)
    description = models.CharField(max_length=250)
    slug = models.SlugField()
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=STATUS.choices,default=STATUS.DRAFT)

    class Meta:
        ordering = ['-publish']
        # indexing
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
