# Generated by Django 4.1.7 on 2023-03-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]