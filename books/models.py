from django.db import models

from django.db import models

from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.utils import timezone


class publishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__gte=1)


class Books(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    published_data = models.DateField()
    quantity = models.IntegerField()
    book_info = models.TextField(default="")
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT, default="1")
    book_img = models.CharField(max_length=255, default="")
    slug = models.SlugField(max_length=255, default="")

    objects = models.Manager()
    published = publishedManager()

    def get_absolute_url(self):
        return reverse("book_info", kwargs={"book_slug": self.slug})


class Genre(models.Model):
    genre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default="", db_index=True)

    class Meta:
        ordering = ["genre"]

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse("selected_catalog", kwargs={"catalog_slug": self.slug})


class Customers(models.Model):
    first_name = models.CharField(max_length=255, default="")
    second_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    phone_number = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Customers"
        verbose_name = "Customer"


from django.db import models
from django.contrib.auth.models import User
from .models import Books


class Orders(models.Model):
    STATUS_CHOICES = [
        ("куплено", "Куплено"),
        ("ожидание", "Ожидание")
    ]
    customer_id = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Books, on_delete=models.PROTECT, default=1)
    price = models.CharField(max_length=200, default="")
    quantity = models.IntegerField(default="")
#
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ожидание")

    def __str__(self):
        return self.book.book_name


class LastOrders(models.Model):
    STATUS_CHOICES = [
        ("ожидание", "Ожидание"),
        ("подтверждено", "Подтверждено"),
        ("отправлено", "Отправлено"),
        ("доставлено", "Доставлено"),
    ]
    customer_id = models.ForeignKey(User, on_delete=models.PROTECT)
    basket = models.ManyToManyField(Orders, related_name="orders", blank=True)
    all_price = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    address = models.CharField(max_length=200, default="")

    class Meta:
        ordering = ["status"]

