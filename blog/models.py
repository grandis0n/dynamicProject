from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=26)
    brief_description = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField('Главное изображение', upload_to='post_images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
