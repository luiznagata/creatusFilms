# Generated by Django 4.1 on 2022-09-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='sinopse',
            field=models.TextField(default='', max_length=5000),
        ),
    ]
