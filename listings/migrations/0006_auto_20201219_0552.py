# Generated by Django 3.1.4 on 2020-12-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='condition',
            field=models.ManyToManyField(to='listings.Condition'),
        ),
    ]
