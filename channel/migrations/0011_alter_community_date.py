# Generated by Django 4.1.4 on 2024-03-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0010_alter_community_options_alter_community_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
