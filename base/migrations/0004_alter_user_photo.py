# Generated by Django 5.0.6 on 2024-07-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='defualtl.svg', null=True, upload_to=''),
        ),
    ]
