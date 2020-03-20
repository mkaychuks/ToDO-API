from django.contrib import admin

# Register your models here.
from todoapp.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'owner')
    fieldsets = [
        (None, {'fields': ['title', 'tag', 'description']})
    ]

admin.site.register(Todo, TodoAdmin)