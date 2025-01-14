from django.contrib import admin

from .models import Geography, Relevance, Skills


@admin.register(Geography)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Relevance)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Skills)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)
