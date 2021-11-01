from django.urls import path,include
from rest_framework import routers
from .views import TeamsViewset
router=routers.DefaultRouter()
router.register(r'teams',TeamsViewset)
urlpatterns = [
    path('', include(router.urls)),
]
