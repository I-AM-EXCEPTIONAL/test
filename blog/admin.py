from django.contrib import admin
from .models import Category, Post, Year


# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'add_date')
    search_fields = ('title',)


class YearAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'add_date')
    search_fields = ('title',)
    list_filter = ('cat','batch')
    list_per_page = 50

    # class Media:
    #     js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Year, YearAdmin)
