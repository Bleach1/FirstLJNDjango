from django.contrib import admin

# Register your models here.
from LJNDjango.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


admin.site.register(Article, ArticleAdmin)
