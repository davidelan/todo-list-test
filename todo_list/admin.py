from django.contrib import admin
from .models import Todo_list, Task
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Task) 
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description')
    search_fields = ['title']
    list_filter = ('title',)
    prepopulated_fields = {'description': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Todo_list)
#admin.site.register(Task)

