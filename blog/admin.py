from django.contrib import admin
from mdeditor.widgets import MDEditorWidget

from .models import *

class PostInline(admin.StackedInline):
    model = Post

class AutorAdmin(admin.ModelAdmin):
    inlines = (PostInline, )

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_filter = ['data_cadastro','autor']

admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)
