from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Otomatis saat dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Otomatis saat diubah
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses_taught"  # Untuk mengakses course dari user.instructor
    )
    subscribers = models.ManyToManyField(
        User,
        related_name="courses_subscribed",  # <-- typo diperbaiki di sini
        blank=True  # Membolehkan course tanpa subscriber
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.99)

    def __str__(self):
        return self.title
