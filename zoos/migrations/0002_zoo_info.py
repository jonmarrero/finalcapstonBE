# Generated by Django 4.1.7 on 2023-03-31 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoo',
            name='info',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]
