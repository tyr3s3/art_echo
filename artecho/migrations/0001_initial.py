# Generated by Django 2.2.28 on 2024-03-03 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('totalPosts', models.IntegerField(default=0)),
                ('totalLikes', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('isAI', models.BooleanField()),
                ('file', models.ImageField(upload_to='')),
                ('likes', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=1000)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='artecho.Category')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='artecho.Image')),
            ],
            options={
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(max_length=128, unique=True)),
                ('profilePicture', models.ImageField(upload_to='')),
                ('bio', models.TextField(max_length=1000)),
                ('forename', models.CharField(max_length=128, unique=True)),
                ('surename', models.CharField(max_length=128, unique=True)),
                ('totalLikes', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('liked', models.ManyToManyField(to='artecho.Image')),
            ],
            options={
                'verbose_name_plural': 'images',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='artecho.User'),
        ),
    ]
