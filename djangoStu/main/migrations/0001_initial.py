# Generated by Django 2.0.4 on 2019-09-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=1000, null=True)),
                ('display_idx', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'main_course',
            },
        ),
    ]