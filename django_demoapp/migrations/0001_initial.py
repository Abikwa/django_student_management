# Generated by Django 3.2.9 on 2021-11-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_responsible', models.CharField(max_length=250)),
                ('adress_responsible', models.CharField(max_length=250)),
                ('phone_numbrer', models.IntegerField(verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=250)),
                ('numbrer_hour', models.IntegerField(verbose_name="Hour' Number")),
                ('status', models.SmallIntegerField(default=1)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_demoapp.responsible')),
            ],
        ),
    ]