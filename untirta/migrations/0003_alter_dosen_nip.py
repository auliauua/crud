# Generated by Django 4.1.2 on 2022-10-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untirta', '0002_alter_dosen_nip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='nip',
            field=models.IntegerField(),
        ),
    ]
