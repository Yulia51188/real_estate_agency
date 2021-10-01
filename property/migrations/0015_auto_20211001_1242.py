# Generated by Django 2.2.20 on 2021-10-01 09:42

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20211001_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterIndexTogether(
            name='owner',
            index_together={('full_name', 'pure_phone')},
        ),
    ]
