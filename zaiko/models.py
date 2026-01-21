from django.db import models

# --- 在庫アイテム ---
class Item(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# --- 入出庫履歴 ---
class StockHistory(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    ACTION_CHOICES = [
        (IN, '入庫'),
        (OUT, '出庫'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='histories')
    action = models.CharField(max_length=3, choices=ACTION_CHOICES)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.get_action_display()} - {self.quantity}"
