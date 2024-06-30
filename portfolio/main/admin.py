from django.contrib import admin
from .models import Tag, Project, projectImage

class projectImageInline(admin.TabularInline):
    model = projectImage
    extra = 1

class projectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [projectImageInline]
    search_fields = ("title", "discription")
    list_filter = ("tags", )

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, projectAdmin)
admin.site.register(projectImage)
