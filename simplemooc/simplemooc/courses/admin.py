from django.contrib import admin
from .models import Courses

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Preenche slug com o nome

admin.site.register(Courses, CourseAdmin)
