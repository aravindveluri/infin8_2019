from django.contrib import admin

# Register your models here.
from stage.models import Stage

# class StageAdmin(admin.ModelAdmin):

admin.site.register(Stage)