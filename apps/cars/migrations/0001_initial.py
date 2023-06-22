# Generated by Django 4.2.2 on 2023-06-19 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autoparks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body_type', models.CharField(max_length=25)),
                ('engine_volume', models.FloatField()),
                ('autopark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='autoparks.autopark')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]