from django.contrib import admin

from test1.models import Posts


# Register your models here.

class StudentDataAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'title', 'published_date')


admin.site.register(Posts, StudentDataAdmin)
