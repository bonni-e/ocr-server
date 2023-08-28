"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from boards.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('boards/', include("boards.urls")),
    path('users/', include("users.urls")),
    path('ocr/', include("ocr.urls")),
]

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', boards.BoardViewSet.as_view({
        'get' : 'list'
    })),
    path('<int:pk>', boards.BoardViewSet.as_view({
        'get' : 'retrieve',
        'post' : 'partial_update',
        'delete' : 'destroy',
    })),
]
'''

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', boards.get_board_all),
    path('', boards.Boards.as_view()),
]
'''

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)