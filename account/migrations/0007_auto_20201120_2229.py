# Generated by Django 3.1.3 on 2020-11-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201114_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='bukti_foto',
            field=models.ImageField(blank=True, null=True, upload_to='bukti_pengenal'),
        ),
    ]