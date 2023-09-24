from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    content = models.TextField()
    preview = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    publication_sign = models.BooleanField(default=True)
    number_of_views = models.IntegerField(default=90)

    def __str__(self):
        return f'Post (pk={self.pk}, name={self.title})'


