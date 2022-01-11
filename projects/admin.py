from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'published_date')
    list_display_links =('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 25
    prepopulated_fields = {
        'slug': ('title',)
        }

admin.site.register(Project, ProjectAdmin)
