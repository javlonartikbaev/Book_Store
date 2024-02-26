from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.urls import reverse


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
    book_img = models.ImageField(upload_to="img/", default="")
    slug = models.SlugField(max_length=255, default="", unique=True, db_index=True)

    objects = models.Manager()
    published = publishedManager()

    def get_absolute_url(self):
        return reverse("book_info", kwargs={"book_slug": self.slug})


class Genre(models.Model):
    genre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default="", db_index=True)

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse("selected_catalog", kwargs={"catalog_slug": self.slug})


class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)


class Orders(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.PROTECT)
    order_date = models.DateField()
    total_price = models.CharField(max_length=100)


class OrderItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.PROTECT)
    book_id = models.ForeignKey(Books, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
