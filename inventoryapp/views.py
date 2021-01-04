from django.http import HttpResponse
from django.shortcuts import render
from inventoryapp.models import Server
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId
from django.views.generic import ListView
import json
from bson.json_util import dumps
from .resources import ServerResource

# Create your views here.
def export(request):
    server_resource = ServerResource()
    dataset = server_resource.export()
    response = HttpResponse(dataset.csv, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="server.xls"'
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="server.csv"'

    return response

class ServerListView(ListView):
    model = Server
    template_name = 'inventoryapp/main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = dumps(list(Server.objects.values()))
        return context


@csrf_exempt
def add_server(request):
    server = Server(server_name=request.POST.get('server_name'), 
                    cluster_name=request.POST.get('cluster_name'), 
                    cluster_version=request.POST.get('cluster_version'), 
                    server_role=request.POST.get('server_role'), 
                    os_version=request.POST.get('os_version'), 
                    ip_address=request.POST.get('ip_address'), 
                    cpus=request.POST.get('cpus'), 
                    memory_in_kb=request.POST.get('memory_in_kb'))
    server.save()
    return HttpResponse("Server Added!")

@csrf_exempt
def update_server(request, id):
    server = Server.objects.get(_id=ObjectId(id))
    server.cluster_name=request.POST.get('cluster_name')
    server.server_role=request.POST.get('server_role')
    server.save()
    return HttpResponse("Server Modified!")

@csrf_exempt
def delete_server(request, id):
    server = Server.objects.get(_id=ObjectId(id))
    server.delete()
    return HttpResponse("Server Deleted!")

def view_server(request, id):
    server = Server.objects.get(_id=ObjectId(id))
    stringValue = "Server Name : " + server.server_name + " Cluster Name : " + server.cluster_name + " Server Role : " + server.server_role
    return HttpResponse(stringValue)

def view_all_server(request):
    servers = Server.objects.all()
    stringValue = ""
    for server in servers:
        stringValue += "Server Name : " + server.server_name + " Cluster Name : " + server.cluster_name + " Server Role : " + server.server_role +"\n"
    return HttpResponse(stringValue)