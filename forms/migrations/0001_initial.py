# Generated by Django 2.1.7 on 2019-06-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='')),
                ('format', models.CharField(max_length=100)),
                ('formatHeight', models.FloatField()),
                ('formatWidth', models.FloatField()),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]