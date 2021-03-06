# Generated by Django 2.1.7 on 2019-02-18 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isFeatured', models.BooleanField(default=False, verbose_name='Promowany')),
                ('name', models.CharField(max_length=150, verbose_name='Tytuł')),
                ('description', models.TextField(verbose_name='Opis')),
                ('photoUrl', models.ImageField(default='/images/cards/default.jpg', upload_to='images/cards/', verbose_name='Zdjęcie')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'verbose_name_plural': 'Kartki',
            },
        ),
    ]
