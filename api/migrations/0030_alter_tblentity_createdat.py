# Generated by Django 3.2.7 on 2021-12-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_tblentity_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblentity',
            name='CreatedAT',
            field=models.DateField(auto_now_add=True),
        ),
    ]
