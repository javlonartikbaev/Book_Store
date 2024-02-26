from django.contrib import admin

# Register your models here.
from .models import Books, Genre, Orders, OrderItems, Customers


class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name', 'price', 'published_data', 'quantity', 'book_info')
    search_fields = ('book_name', 'author_name')


admin.site.register(Books, BooksAdmin)
admin.site.register(Genre)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Customers)
