# Generated by Django 2.1.7 on 2019-03-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovelace', '0013_auto_20190319_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiras',
            name='imagem',
            field=models.CharField(default='', max_length=250),
        ),
    ]
