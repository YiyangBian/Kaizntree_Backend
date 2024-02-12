from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    # 可以根据需要添加更多字段，例如描述、父分类等

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    available_stock = models.DecimalField(max_digits=10, decimal_places=2)
    # 根据需要添加更多字段，例如价格、尺寸、颜色等

    def __str__(self):
        return self.name
