# Generated by Django 4.1.7 on 2024-12-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client_name',
            field=models.CharField(default='Unknown Client', max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client_phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]