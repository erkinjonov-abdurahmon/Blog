from django.contrib import admin
from . import models


@admin.register(models.BaseModel)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at']
    list_display_links = ['created_at', 'updated_at']


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']