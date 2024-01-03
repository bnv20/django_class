from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'keyword')  # Customize as needed
    search_fields = ['title', 'keyword']

admin.site.register(News, NewsAdmin)

# Register your models here.
