# Generated by Django 4.2.2 on 2023-06-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notes', models.TextField()),
                ('Files', models.FileField(blank=True, max_length=300, null=True, upload_to='files')),
            ],
        ),
    ]
