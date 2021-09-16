from django.db import migrations


def set_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    construction_year_limit = 2015
    flats = Flat.objects.all()
    for flat in flats:
        flat.new_building = flat.construction_year > construction_year_limit
        flat.save()


def set_none_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        flat.new_building = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20210916_0731'),
    ]

    operations = [
        migrations.RunPython(set_new_building_field, set_none_new_building),
    ]
