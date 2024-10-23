from django.core.management.base import BaseCommand
import pandas as pd
from transactions.models import Client, Transaction

class Command(BaseCommand):
    help = 'Run ETL process to load data from CSV and XLSX files into the database'

    def handle(self, *args, **kwargs):
        # Extract: Read the CSV and Excel files
        clients_df = pd.read_csv('clients.csv')
        transactions_df = pd.read_excel('transactions.xlsx')

        # Load clients data into the Client model
        for _, row in clients_df.iterrows():
            Client.objects.update_or_create(
                client_id=row['client_id'],
                defaults={
                    'name': row['name'],
                    'email': row['email'],
                    'date_of_birth': row['date_of_birth'],
                    'country': row['country'],
                    'account_balance': row['account_balance']
                }
            )

        # Load transactions data into the Transaction model
        for _, row in transactions_df.iterrows():
            Transaction.objects.update_or_create(
                transaction_id=row['transaction_id'],
                defaults={
                    'client_id': row['client_id'],
                    'transaction_type': row['transaction_type'],
                    'transaction_date': row['transaction_date'],
                    'amount': row['amount'],
                    'currency': row['currency']
                }
            )

        self.stdout.write(self.style.SUCCESS('ETL process completed successfully!'))
