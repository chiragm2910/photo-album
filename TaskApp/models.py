from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Album(TimeStampMixin):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.name


class Photo(TimeStampMixin):
    user = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(max_length=200)
    albums = models.ManyToManyField(Album, related_name='photos', blank=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.user
