"""D_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView #呈现给定模板

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls','blog'),namespace='blog')),  # 新增
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'), # 新增
    path('article/', include(('article.urls', 'article'), namespace='article')),
    path('image/', include('image.urls')),

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)