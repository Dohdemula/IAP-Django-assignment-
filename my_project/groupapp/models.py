from django.db import models

# Create your models here.
class Ticket(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.event_name