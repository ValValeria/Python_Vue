from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, Comment
from django.utils.html import format_html

admin.site.unregister(User)


class CommentInstanceInline(admin.TabularInline):
    model = Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'time', 'post_link', "user")
    search_fields = ('content', )

    def comment(self, obj):
        content = obj.content.split(" ")
        short_content = " ".join(content[0:10])
        return short_content

    def user(self, obj):
        return format_html('<a href={} class="btn-link">{}</a>', "/admin/auth/user/{}/change/".format(obj.user.id), obj.user.username)

    def post_link(self, obj):
        return format_html('<a href={} class="btn-link">View post</a>', "/admin/auth/post/{}/change/".format(obj.id));


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ID', "email", "role", "last_join", "comments", "likes")
    list_filter = ('email',)
    search_fields = ('email', 'first_name', 'last_name', 'role')

    def ID(self, obj):
        return format_html('<a href={} class="btn-link">{}</a>', "/admin/auth/user/{}/change/".format(obj.id), obj.id);

    def role(self, obj):
        user_role = 'user'

        if obj.is_superuser:
            user_role = 'admin'

        return user_role

    def last_join(self, obj):
        return obj.last_login

    def get_queryset(self, request):
        return super().get_queryset(request).exclude(id=request.user.id)

    def likes(self, obj):
        return obj.post_set.all().count()

    def comments(self, obj):
        return obj.comment_set.all().count()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "likes", "comments", "view")
    search_fields = ("title", "category", "content")
    inlines = [CommentInstanceInline]

    def view(self, obj):
        return format_html('<a href={} class="btn-link">{}</a>', "/admin/app/post/{}/change/".format(obj.id), 'View')

    def category(self, obj):
        return obj.categories

    def likes(self, obj):
        return obj.users_likes.all().count()

    def comments(self, obj):
        return obj.comment_set.all().count()


admin_title = "Admin Panel"
admin.site.site_header = admin_title  # default: "Django Administration"
admin.site.index_title = admin_title  # default: "Site administration"
admin.site.site_title = admin_title + "Admin"  # default: "Django site admin"
