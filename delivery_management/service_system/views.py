from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Component, Vehicle, Issue, Transaction
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer, TransactionSerializer
from datetime import datetime, timedelta
from django.db.models import Sum

# Create your views here.

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['post'])
    def create_transaction(self, request):
        vehicle_id = request.data.get('vehicle_id')
        vehicle = Vehicle.objects.get(id=vehicle_id)
        issues = vehicle.issues.all()
        total_cost = sum(issue.get_cost() for issue in issues)
        transaction = Transaction.objects.create(vehicle=vehicle, total_cost=total_cost)
        serializer = self.get_serializer(transaction)
        return Response(serializer.data)

    @api_view(['GET'])
    def revenue_view(request):
        # Daily revenue
        today = datetime.today()
        last_7_days = today - timedelta(days=7)
        daily = Transaction.objects.filter(created_at__gte=last_7_days).values('created_at__date').annotate(revenue=Sum('total_cost')).order_by('created_at__date')

        # Monthly revenue
        monthly = Transaction.objects.all().values('created_at__month').annotate(revenue=Sum('total_cost')).order_by('created_at__month')

        # Yearly revenue
        yearly = Transaction.objects.all().values('created_at__year').annotate(revenue=Sum('total_cost')).order_by('created_at__year')

        response = {
            'daily': [{'date': d['created_at__date'], 'revenue': d['revenue']} for d in daily],
            'monthly': [{'month': d['created_at__month'], 'revenue': d['revenue']} for d in monthly],
            'yearly': [{'year': d['created_at__year'], 'revenue': d['revenue']} for d in yearly],
        }
        return Response(response)
