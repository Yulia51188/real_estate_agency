# Generated by Django 2.2.20 on 2021-09-17 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20210916_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_appeals', to='property.Flat', verbose_name='Квартира')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_appeals', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
