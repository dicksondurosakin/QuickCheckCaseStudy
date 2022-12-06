from django.db import models

# Create your models here.


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=250)
    by = models.CharField(max_length=250)
    time = models.DateTimeField()
    text = models.TextField()

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return f"{self.id}"
