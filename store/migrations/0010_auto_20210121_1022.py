# Generated by Django 3.1.5 on 2021-01-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_shippingaddress_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]