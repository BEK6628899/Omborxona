# Generated by Django 4.1.7 on 2023-02-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0002_alter_mahsulot_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='nom',
            field=models.CharField(max_length=50),
        ),
    ]
