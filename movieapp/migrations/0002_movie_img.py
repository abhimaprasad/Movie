# Generated by Django 3.1.4 on 2024-01-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ffgjk', upload_to='pics'),
            preserve_default=False,
        ),
    ]
