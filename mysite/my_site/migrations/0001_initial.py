# Generated by Django 2.1.3 on 2018-11-10 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio_title', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('git_link', models.URLField(default='https://github.com/vitogalv')),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='places')),
                ('article', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=300)),
                ('city', models.CharField(default='City', max_length=50)),
                ('state', models.CharField(default='State', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('summary', models.TextField()),
                ('git_link', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='projects')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('industry', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, unique=True)),
                ('resume', models.ManyToManyField(to='my_site.Resume')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.Place'),
        ),
        migrations.AddField(
            model_name='duty',
            name='position',
            field=models.ManyToManyField(to='my_site.Position'),
        ),
    ]
