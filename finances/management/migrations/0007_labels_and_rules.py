# Generated by Django 2.0.10 on 2019-04-04 16:38

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20190210_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_conditional', models.CharField(choices=[('c', 'Contains'), ('p', 'Prefix'), ('s', 'Sufix'), ('r', 'Regular expresion'), ('g', 'Greater than'), ('G', 'Greater or equal than'), ('L', 'Lower or equal than'), ('l', 'Lower than')], max_length=1)),
                ('conditional', models.CharField(max_length=200)),
                ('negate', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_labels', models.ManyToManyField(to='management.Label')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='management.Rule')),
            ],
        ),
        migrations.CreateModel(
            name='RuleAndCondition',
            fields=[
                ('abstractcondition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.AbstractCondition')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conditions', to='management.Rule')),
            ],
            bases=('management.abstractcondition',),
        ),
        migrations.CreateModel(
            name='RuleOrCondition',
            fields=[
                ('abstractcondition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.AbstractCondition')),
                ('orCondition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orConditions', to='management.RuleAndCondition')),
            ],
            bases=('management.abstractcondition',),
        ),
    ]
