from django.contrib import admin
from .models import Post, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rating')
    list_display_links = ('id', 'user')
    search_fields = ('rating',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_author', 'post_content', 'post_name', 'post_time_in')
    list_display_links = ('id',)
    search_fields = ('post_name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)


# Register your models here.
