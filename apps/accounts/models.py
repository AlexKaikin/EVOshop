from django.db import models
from django.contrib.auth.models import AbstractUser
from pytils import translit


def get_avatar_file_path(instance, filename):
    return '{0}/{1}/{2}'.format('profile', instance.username, filename)


class Profile(AbstractUser):
    """ Профиль пользователя """

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.FileField(upload_to=get_avatar_file_path, null=True, blank=True, verbose_name='Ваше фото')
    slug = models.SlugField(max_length=200, db_index=True, blank=True, unique=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        name = self.username
        self.slug = translit.slugify(name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
