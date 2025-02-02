# Generated by Django 4.1.4 on 2024-03-16 23:29

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('full_name', models.CharField(max_length=256)),
                ('channel_name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('disable', 'Disable')], default='active', max_length=100)),
                ('keywords', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('subscribers', models.ManyToManyField(related_name='user_subs', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
