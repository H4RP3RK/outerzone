# Generated by Django 3.1.3 on 2020-11-23 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('products', '0007_auto_20201123_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artists.artist'),
        ),
    ]