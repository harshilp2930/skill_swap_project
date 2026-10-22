from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill_type', 'created_at')
    list_filter = ('skill_type',)
    search_fields = ('title', 'description')