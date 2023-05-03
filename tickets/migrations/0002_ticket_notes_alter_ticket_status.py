# Generated by Django 4.1.7 on 2023-05-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('resolved', 'Resolved')], default='Open', max_length=255),
        ),
    ]
