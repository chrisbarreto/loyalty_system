# dashboard/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardAnalyticsViewSet

router = DefaultRouter()
router.register(r'dashboard-analitico', DashboardAnalyticsViewSet, basename='dashboard-analitico')

urlpatterns = [
    path('', include(router.urls)),
]
