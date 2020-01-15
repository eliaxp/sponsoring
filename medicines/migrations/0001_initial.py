# Generated by Django 2.2.5 on 2019-09-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('Laboratory', models.CharField(db_index=True, max_length=100, verbose_name='Laboratory')),
                ('description', models.TextField(blank=True, default='', help_text='Write some descriptive words about this medicine.', max_length=2000, verbose_name='Description')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Medicines/', verbose_name='Medicine image')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
                'ordering': ['-date_created'],
            },
        ),
    ]