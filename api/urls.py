from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tbltib', views.TibView)

urlpatterns = [
    path('', views.index, name="index"),                    # Home page
    path('offline.html', views.offline, name='offline'),    # Offline page
    path('api/', include(router.urls)),
]
