# Generated by Django 4.2.4 on 2023-11-05 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('dep_description', models.TextField()),
                ('dep_slug', models.SlugField(unique=True)),
                ('dep_image', models.ImageField(upload_to='picture')),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_slug', models.SlugField(unique=True)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointments.departments')),
            ],
        ),
    ]
