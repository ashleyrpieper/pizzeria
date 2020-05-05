from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A type of pizza."""
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return pizza names."""
        return self.name

class Topping(models.Model):
    """Topings on a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return pizza type & topping name."""
        return self.name