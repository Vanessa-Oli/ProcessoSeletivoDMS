# Generated by Django 4.0.3 on 2022-03-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time1', models.CharField(blank=True, max_length=100, null=True)),
                ('time2', models.CharField(blank=True, max_length=20, null=True)),
                ('local', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('goltime1', models.IntegerField(blank=True, default=0, null=True)),
                ('goltime2', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'copa',
            },
        ),
    ]
