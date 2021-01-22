# Generated by Django 3.1.5 on 2021-01-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210121_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]