"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventoryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_server/', views.add_server),
    path('update_server/<str:id>', views.update_server),
    path('delete_server/<str:id>', views.delete_server),
    path('view_server/<str:id>', views.view_server),
    path('view_all_server/', views.view_all_server),
    path('', views.ServerListView.as_view(), name='main-view'),
    path('export-csv/', views.export, name='export'),
]
