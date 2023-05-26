from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TicketStatus(models.TextChoices):
    OPEN = 'Open'
    RESOLVED = 'resolved'



class TicketType(models.TextChoices):
    INQUIRY = 'inquiry'
    PRODUCT_SUPPORT = 'product support'
    COMPLAINT = 'complaint'


class Ticket(models.Model):
    # the user who created the ticket
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    # the assigned user
    assigned_user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=TicketStatus.choices, default=TicketStatus.OPEN)
    ticket_type = models.CharField(max_length=255, choices=TicketType.choices, null=True, blank=True)

    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        """Represent a ticket by the title"""
        return self.title

    def save(self, *args, **kwargs):
        """Ensure that validation occurs for every Ticket model save."""
        self.full_clean(exclude=None)
        super().save(*args, **kwargs)

    class Meta(object):
        """Sort tickets alphabetically by date."""

        ordering = ('title',)
