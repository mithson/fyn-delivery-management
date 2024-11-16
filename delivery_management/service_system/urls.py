from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComponentViewSet, VehicleViewSet, IssueViewSet, TransactionViewSet

router = DefaultRouter()
router.register('components', ComponentViewSet)
router.register('vehicles', VehicleViewSet)
router.register('issues', IssueViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
