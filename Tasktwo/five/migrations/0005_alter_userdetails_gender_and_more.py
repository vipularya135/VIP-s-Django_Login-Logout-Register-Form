# Generated by Django 5.0.1 on 2024-01-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('five', '0004_alter_userqualifications_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='userqualifications',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userqualifications',
            name='education',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userqualifications',
            name='hobbies',
            field=models.TextField(blank=True, default=''),
        ),
    ]
