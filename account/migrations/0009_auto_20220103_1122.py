# Generated by Django 3.2.8 on 2022-01-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='T1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='T2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]
