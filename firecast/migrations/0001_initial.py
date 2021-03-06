# Generated by Django 2.1.2 on 2018-10-24 12:40

import autoslug.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='images/default.png', upload_to='images/')),
                ('audio', models.FileField(upload_to='audio/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['wav', 'mp3', 'ogg'])])),
            ],
        ),
    ]
