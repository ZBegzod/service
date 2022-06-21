# Generated by Django 4.0.4 on 2022-06-01 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fast_food_branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fast_food_branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.fast_food_branch')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.product')),
            ],
        ),
    ]
