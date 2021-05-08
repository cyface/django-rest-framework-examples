# Generated by Django 3.2.2 on 2021-05-08 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('cover_art', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PodcastPersonRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person', to='podcasts.person')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='podcast', to='podcasts.podcast')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='role', to='podcasts.role')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ManyToManyField(related_name='people', through='podcasts.PodcastPersonRole', to='podcasts.Role'),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='')),
                ('sequence', models.IntegerField()),
                ('show_notes', models.TextField()),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='podcasts.podcast')),
            ],
        ),
    ]