from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TICKET_STATUS = (
    ('OPEN', 'open'),
    ('RESOLVED', 'resolved'),
    ('ARCHIVED', 'ARCHIVED'),
)

TICKET_TYPES = (
    ('INQUIRY', 'inquiry'),
    ('PRODUCT_SUPPORT', 'product support'),
    ('COMPLAINT', 'complaint'),
)

class Ticket(models.Model):
    # the user who created the ticket
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    # the assigned user
    assigned_user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=TICKET_STATUS, default='OPEN')
    ticket_type = models.CharField(max_length=255, choices=TICKET_TYPES, null=True, blank=True)

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
