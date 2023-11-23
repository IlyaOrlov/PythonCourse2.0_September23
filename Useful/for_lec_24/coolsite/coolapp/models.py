from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Film(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)

    def __str__(self):
        return f"{self.name}: {self.desc}"
