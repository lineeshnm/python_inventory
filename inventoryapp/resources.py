from import_export import resources
from .models import Server

class ServerResource(resources.ModelResource):
    class Meta:
        model = Server
        skip_unchanged = True
        report_skipped = True
        exclude = ('_id',)
        import_id_fields = ('server_name', 'cluster_name', 'cluster_version', 'server_role', 'os_version', 'ip_address', 'cpus', 'memory_in_kb')