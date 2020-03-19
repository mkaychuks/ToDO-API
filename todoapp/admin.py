from django.contrib import admin

# Register your models here.
from todoapp.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'owner')
    fieldsets = [
        (None, {'fields': ['title', 'tag', 'description']})
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()


admin.site.register(Todo, TodoAdmin)