# Generated by Django 3.1.8 on 2023-02-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20230217_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_state',
            field=models.CharField(choices=[('UNRESOLVED', 'Unresolved'), ('REJECTED', 'Rejected'), ('ACCEPTED', 'Accepted')], default='UNRESOLVED', max_length=30),
        ),
    ]