# Generated by Django 5.1.1 on 2024-10-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0005_alter_addvehicle_name_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvehicle',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='addvehicle',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='myimage'),
        ),
    ]
