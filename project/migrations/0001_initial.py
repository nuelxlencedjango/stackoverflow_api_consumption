# Generated by Django 3.2 on 2022-05-13 20:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('search', models.CharField(max_length=100)),
                ('date_searched', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner_id', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=500)),
                ('profile', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('owner_name', models.CharField(max_length=200)),
                ('owner_link', models.CharField(max_length=1000)),
                ('is_answer', models.BooleanField(default=False)),
                ('view_count', models.CharField(max_length=200)),
                ('question_id', models.CharField(max_length=100)),
                ('stflow_link', models.CharField(max_length=100)),
                ('last_activity_date', models.CharField(max_length=100)),
                ('creation_date', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
    ]
