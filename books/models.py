from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300, verbose_name="书名")
    author = models.CharField(max_length=100, verbose_name="作者")
    publication_date = models.DateField(verbose_name="出版日期")
    def __str__(self):
        return self.title