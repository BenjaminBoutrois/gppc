# Generated by Django 2.1.7 on 2019-06-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20190602_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]