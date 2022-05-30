# Generated by Django 4.0.4 on 2022-05-29 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0004_remove_category_image_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_category',
        ),
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Media.category'),
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_location',
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Media.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
