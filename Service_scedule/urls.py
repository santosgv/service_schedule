from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Core.views import agenda

router = routers.DefaultRouter()
router.register(r'agenda', agenda)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls )),
]
