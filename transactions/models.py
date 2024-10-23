from django.db import models

class Client(models.Model):
    client_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=4, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

