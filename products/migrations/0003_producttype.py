# Generated by Django 4.1.4 on 2022-12-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=250)),
                ('type_id', models.PositiveBigIntegerField()),
            ],
        ),
    ]
