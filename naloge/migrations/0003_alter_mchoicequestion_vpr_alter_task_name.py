# Generated by Django 4.2.7 on 2023-11-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naloge', '0002_mchoicetask_mchoicequestion_mchoiceanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mchoicequestion',
            name='vpr',
            field=models.CharField(max_length=500, verbose_name='vprašanje'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
