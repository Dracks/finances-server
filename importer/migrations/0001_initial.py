# Generated by Django 2.0.1 on 2018-01-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawDataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('movement_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('date_value', models.DateField(null=True)),
                ('details', models.TextField(null=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rawdatasource',
            unique_together={('kind', 'movement_name', 'date', 'value')},
        ),
    ]
