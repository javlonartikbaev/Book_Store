from django.contrib import admin

# Register your models here.
from .models import Books, Genre, Orders, Customers, LastOrders


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        "book_name",
        "author_name",
        "price",
        "published_data",
        "quantity",
        "book_info",
        "slug"
    )
    search_fields = ("book_name", "author_name")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer_id_id", "book_id", "price", "quantity", 'status')


class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre", 'slug')


class LastOrderAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "display_books", "all_price", "created_at", "status", "address")

    def display_books(self, obj):
        return ", ".join([book.book.book_name for book in obj.basket.all()])


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "email", "phone_number")


admin.site.register(Books, BooksAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(LastOrders, LastOrderAdmin)

admin.site.register(Customers, CustomerAdmin)
