# Generated by Django 3.2.8 on 2022-01-03 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_t2_name1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t2',
            old_name='name1',
            new_name='name',
        ),
    ]
