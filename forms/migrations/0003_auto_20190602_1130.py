# Generated by Django 2.1.7 on 2019-06-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_contactdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='formatHeight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='formatWidth',
            field=models.FloatField(null=True),
        ),
    ]
