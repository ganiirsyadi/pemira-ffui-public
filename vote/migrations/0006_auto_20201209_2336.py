# Generated by Django 3.1.3 on 2020-12-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_vote2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote2',
            name='bem_vote',
            field=models.CharField(default='0', max_length=1),
            preserve_default=False,
        ),
    ]
