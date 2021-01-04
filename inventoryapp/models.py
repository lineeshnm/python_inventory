from djongo import models

class Server(models.Model):
    # _id=models.ObjectIdField()
    server_name=models.CharField(max_length=100, unique=True)
    cluster_name=models.CharField(max_length=20)
    cluster_version=models.CharField(max_length=10)
    server_role=models.CharField(max_length=50)
    os_version=models.CharField(max_length=30)
    ip_address=models.CharField(max_length=16)
    cpus=models.IntegerField()
    memory_in_kb=models.IntegerField()
    objects=models.DjongoManager()

    def __str__(self):
        return str(self.server_name + " " + self.cluster_name + " " + self.cluster_version + " " + self.server_role)