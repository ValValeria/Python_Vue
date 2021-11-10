from django.contrib import admin
from .models import Post
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "categories", "view")
    search_fields = ("title", "categories", "content")

    def view(self, obj):
        return format_html('<a href={} class="btn-link">{}</a>', "/admin/auth/post/{}/change/".format(obj.id), 'View')


admin_title = "MyVideo"
admin.site.site_header = admin_title  # default: "Django Administration"
admin.site.index_title = admin_title  # default: "Site administration"
admin.site.site_title = admin_title + "Admin"  # default: "Django site admin"
