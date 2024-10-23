from rest_framework import viewsets
from rest_framework.response import Response
from transactions.models import Transaction
from django.utils.dateparse import parse_date

class TransactionViewSet(viewsets.ViewSet):
    def list(self, request, client_id):
        transactions = Transaction.objects.filter(client_id=client_id)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date:
            transactions = transactions.filter(transaction_date__gte=parse_date(start_date))
        if end_date:
            transactions = transactions.filter(transaction_date__lte=parse_date(end_date))
        
        return Response([t.transaction_id for t in transactions])

