from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
Group = get_user_model()


class Post(models.Model, Group.__str__()):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        slug = models.SlugField(),
        related_name='group',
        blank=True,
        null=True,
        unique=True
    )


class Group(models.Model):
    title = models.TextField()
    slug = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.slug
