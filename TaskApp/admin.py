from django.contrib import admin
from .models import Photo, Album


class ModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Photo, ModelAdmin)
admin.site.register(Album, ModelAdmin)
