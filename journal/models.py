from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entry')  # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='journal_likes', blank=True)  # noqa

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Reply(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')  # noqa
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    report = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
