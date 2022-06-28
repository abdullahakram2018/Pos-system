# Generated by Django 3.2.8 on 2022-01-01 15:39

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.CharField(max_length=200)),
                ('hb', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('lb', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=6)),
                ('trname', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to=account.models.customer_photo_directory)),
                ('note', models.TextField(null=True)),
                ('adderss', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('tele', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('whatsapp', models.CharField(max_length=20, null=True)),
                ('web', models.CharField(max_length=190, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=190)),
                ('adderss', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('tele', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('whatsapp', models.CharField(max_length=20, null=True)),
                ('web', models.CharField(max_length=190, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_branch_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_company_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_company_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('code', models.CharField(max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_currency_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_currency_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(null=True)),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('finance', models.CharField(max_length=190, null=True)),
                ('success', models.BooleanField(default=False)),
                ('attached', models.ImageField(upload_to=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_order_set', to=settings.AUTH_USER_MODEL)),
                ('creditor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.account')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.currency')),
                ('debitor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaves', to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='TypePro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_typepro_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_typepro_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=190)),
                ('name', models.CharField(max_length=190)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_unit_set', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.typepro')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_unit_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, null=True)),
                ('place', models.CharField(max_length=190, null=True)),
                ('tele', models.CharField(max_length=190, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_store_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_store_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=190, null=True)),
                ('name_en', models.CharField(max_length=190, null=True)),
                ('address_ar', models.CharField(max_length=190, null=True)),
                ('address_en', models.CharField(max_length=190, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('start', models.CharField(max_length=190, null=True)),
                ('note_ar', models.TextField(null=True)),
                ('note_en', models.TextField(null=True)),
                ('email', models.CharField(max_length=190, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('tele', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('whatsapp', models.CharField(max_length=20, null=True)),
                ('web', models.CharField(max_length=190, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_project_set', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.typepro')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_project_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('group', models.CharField(max_length=190)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=6)),
                ('package', models.FloatField(null=True)),
                ('la', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('ha', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('puprice', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('sprice', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('company_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.company')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_produt_set', to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.unit')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_product_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('note', models.TextField(null=True)),
                ('success', models.BooleanField(default=False)),
                ('attached', models.ImageField(upload_to=None)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.product')),
                ('stors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.store')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.unit')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.typepro'),
        ),
        migrations.AddField(
            model_name='order',
            name='update_by',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_order_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_exchange_set', to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.currency')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_exchange_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.project'),
        ),
        migrations.AddField(
            model_name='branch',
            name='update_by',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_branch_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.branch'),
        ),
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_account_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.typepro'),
        ),
        migrations.AddField(
            model_name='account',
            name='update_by',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_account_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaves', to=settings.AUTH_USER_MODEL),
        ),
    ]
