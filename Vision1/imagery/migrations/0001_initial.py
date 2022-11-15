# Generated by Django 4.0.6 on 2022-11-02 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chiffrement',
            fields=[
                ('chiffrement_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_source', models.ImageField(blank=True, null=True, upload_to='image_sources/%y/%m/%d')),
                ('image_txt', models.ImageField(blank=True, null=True, upload_to='image_txts/%y/%m/%d')),
                ('image_chiffree', models.ImageField(blank=True, null=True, upload_to='image_chiffrees/%y/%m/%d')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dechiffrement',
            fields=[
                ('dechiffrement_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_chiffree', models.ImageField(blank=True, null=True, upload_to='image_sources/%y/%m/%d')),
                ('image_txt_dechiffrement', models.ImageField(blank=True, null=True, upload_to='image_txts/%y/%m/%d')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('ref_chiffrement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='imagery.chiffrement')),
            ],
        ),
    ]