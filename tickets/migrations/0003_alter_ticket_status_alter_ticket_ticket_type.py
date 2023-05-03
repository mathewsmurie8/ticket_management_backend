# Generated by Django 4.1.7 on 2023-05-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_notes_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPEN', 'open'), ('RESOLVED', 'resolved'), ('ARCHIVED', 'ARCHIVED')], default='OPEN', max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(blank=True, choices=[('INQUIRY', 'inquiry'), ('PRODUCT_SUPPORT', 'product support'), ('COMPLAINT', 'complaint')], max_length=255, null=True),
        ),
    ]