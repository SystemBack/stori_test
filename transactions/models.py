from django.db import models

# Create your models here.

class Update(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(default=None)
    transactions_amount = models.IntegerField(default=None, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100)
    transaction_date = models.CharField(max_length=100)
    transaction = models.CharField(max_length=100)
    is_credit_card = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update = models.ForeignKey(Update, on_delete=models.CASCADE)

    def __str__(self):
        return self.transaction_id
