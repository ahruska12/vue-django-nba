# Generated by Django 3.0.7 on 2023-04-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbaApp', '0002_auto_20230401_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=50),
        ),
    ]