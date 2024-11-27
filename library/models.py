from datetime import timedelta
from time import timezone

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from datetime import datetime, timedelta


class CustomUser(AbstractUser):
    personal_number = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add a related_name to avoid conflict
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Add a related_name to avoid conflict
        blank=True,
    )


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(default="No description available")
    release_date = models.DateField(default="2000-01-01")
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    expires_at = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def save(self, *args, **kwargs):
        if not self.id:  # if this is a new reservation
            self.expires_at = timezone.now() + timedelta(days=1)  # 1-day reservation
        super().save(*args, **kwargs)
