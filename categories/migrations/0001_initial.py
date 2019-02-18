# Generated by Django 2.1.7 on 2019-02-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nazwa kategorii')),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
            },
        ),
    ]
