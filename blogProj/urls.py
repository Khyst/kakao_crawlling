"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.home, name='home'), # views를 import함
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    path('Update/', portfolio.views.imageCrawlling, name="imgCrwalling"),
    path('Delete/ <int:delete_id>', portfolio.views.delete_single_portfolio, name='custom_delete'),
    path('delete_all/', portfolio.views.delete_portfolio, name='deleteAll'),
    path('initial/', portfolio.views.initializer, name='initial'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)