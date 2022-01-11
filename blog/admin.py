from django.contrib import admin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'is_published', 'published_date')
    list_display_links =('id', 'author')
    list_editable = ('is_published',)
    list_per_page = 25
    prepopulated_fields = {
        'slug': ('title',)
        }

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
