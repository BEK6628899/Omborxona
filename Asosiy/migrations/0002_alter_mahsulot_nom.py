# Generated by Django 4.1.7 on 2023-02-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='nom',
            field=models.CharField(max_length=30),
        ),
    ]