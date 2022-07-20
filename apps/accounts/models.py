from django.db import models
from django.contrib.auth.models import AbstractUser


def get_avatar_file_path(instance, filename):
    return '{0}/{1}/{2}'.format('profile', instance.username, filename)


class Profile(AbstractUser):
    """ Профиль пользователя """

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.FileField(upload_to=get_avatar_file_path, null=True, blank=True,
                              verbose_name='Ваше фото')

    def __str__(self):
        return self.username
