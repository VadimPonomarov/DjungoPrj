# Generated by Django 4.2.2 on 2023-06-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_options_alter_car_id_alter_car_model_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={},
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('SUV', 'Suv'), ('Coupe', 'Coupe')], max_length=25),
        ),
    ]
