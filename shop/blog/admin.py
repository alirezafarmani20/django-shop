from django.contrib import admin
from .models import*
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','created','status','slug']
    ordering = ['author','status']
    list_filter = ['author','created','status']
    search_fields = ['author','title','slug','created','status']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {
        'slug': ['title']
    }
    list_editable = ['status','author']
    list_display_links = ['slug']
