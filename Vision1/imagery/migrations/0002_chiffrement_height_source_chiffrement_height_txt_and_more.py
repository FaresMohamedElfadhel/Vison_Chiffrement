# Generated by Django 4.0.6 on 2022-11-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chiffrement',
            name='height_source',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='chiffrement',
            name='height_txt',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='chiffrement',
            name='txt',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='chiffrement',
            name='width_source',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='chiffrement',
            name='width_txt',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='chiffrement',
            name='image_chiffree',
            field=models.ImageField(blank=True, null=True, upload_to='image_chiffrees/'),
        ),
        migrations.AlterField(
            model_name='chiffrement',
            name='image_source',
            field=models.ImageField(blank=True, null=True, upload_to='image_sources'),
        ),
        migrations.AlterField(
            model_name='chiffrement',
            name='image_txt',
            field=models.ImageField(blank=True, null=True, upload_to='image_txts/'),
        ),
    ]
