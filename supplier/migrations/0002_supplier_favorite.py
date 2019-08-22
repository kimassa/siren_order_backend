# Generated by Django 2.2.1 on 2019-08-06 08:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='Supplier_favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]