from django.urls import path, include
from rest_framework import routers
from interview_task.views import TaskViewSet, TileViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tiles', TileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
