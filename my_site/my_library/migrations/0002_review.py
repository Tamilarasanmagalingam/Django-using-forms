# Generated by Django 5.0.3 on 2024-03-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
