from django.db import models

class TransactionItems(models.Model):
    transaction = models.ForeignKey("Transactions", on_delete=models.CASCADE)
    item = models.ForeignKey("Items", on_delete=models.CASCADE)