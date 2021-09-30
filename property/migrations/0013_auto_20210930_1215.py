# Generated by Django 2.2.20 on 2021-09-30 09:15

from django.db import migrations


def copy_owners_from_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    print()
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            full_name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone,
        )


def delete_all_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.RunPython(
            copy_owners_from_flats,
            delete_all_owners
        )
    ]
