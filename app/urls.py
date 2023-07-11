"""
URL configuration for studyhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import submit_material, material_list, material_category, material_search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('submit/', submit_material, name='submit_material'),  # URL pattern for submitting material
    path('', material_list, name='material_list'),  # URL pattern for material list
    path('category/<int:category_id>/', material_category, name='material_category'),  # URL pattern for material category
    path('search/', material_search, name='material_search'),  # URL pattern for material search
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files during development

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
