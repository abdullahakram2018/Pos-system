# Generated by Django 3.2.8 on 2022-01-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_rename_name1_t2_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='t1',
            name='a',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
