from django.contrib import admin
from .models import Ticket
from import_export.admin import ImportExportModelAdmin

class TicketAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'user', 'ticket_type')
    list_display_links = ('id', 'title', 'description', 'status', 'user', 'ticket_type')
    search_fields = ('id', 'title', 'description', 'status', 'user', 'ticket_type')
    list_per_page = 25

admin.site.register(Ticket, TicketAdmin)
