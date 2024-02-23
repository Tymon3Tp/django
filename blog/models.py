from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    STATUS_CHOICES = (
    ('draft','Draft'),
    ('published','Opublikowany')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')

    slug = models.SlugField(max_length=250, unique_for_date='publish')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
