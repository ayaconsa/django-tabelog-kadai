# Generated by Django 5.0 on 2024-03-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NagoyameshiApp', '0002_alter_booking_number_of_persons'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='氏名'),
        ),
    ]
