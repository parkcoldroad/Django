"""
URL configuration for myproject project.

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path , include

# API 엔드포인트에 대한 URL을 자동 생성해주며, 관련 뷰와 그 뷰에 대한 표준 CRUD 작업을 쉽게 설정하기 위해서 defaultRouter객체 사용
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload.urls')),
    path('', include('essay.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
