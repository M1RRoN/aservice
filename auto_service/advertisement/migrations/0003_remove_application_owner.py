# Generated by Django 4.1.7 on 2023-03-14 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='owner',
        ),
    ]
