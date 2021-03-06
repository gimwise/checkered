# Generated by Django 4.0.1 on 2022-04-26 15:17

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Closet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('detail', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='closets.category')),
            ],
        ),
    ]
