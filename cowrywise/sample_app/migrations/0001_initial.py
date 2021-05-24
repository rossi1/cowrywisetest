# Generated by Django 3.2.3 on 2021-05-24 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_uuid', models.UUIDField(unique=True, verbose_name='random_uuid')),
                ('time_stamp', models.DateTimeField(auto_now_add=True, verbose_name='time_stamp')),
            ],
            options={
                'verbose_name': 'uuid_store',
                'ordering': ('-time_stamp',),
            },
        ),
    ]
