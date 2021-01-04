from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Server

@admin.register(Server)
class ServerAdmin(ImportExportModelAdmin):
    list_display = ("server_name", "cluster_name", "cluster_version", "server_role")
    pass

# # Register your models here.
# admin.site.register(Server, ServerAdmin)