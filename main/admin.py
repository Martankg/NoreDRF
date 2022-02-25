from csv import list_dialects
from django.contrib import admin
from main.models import Note

# Register your models here.



class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','creatd_at','updated_at')

admin.site.register(Note, NoteAdmin)