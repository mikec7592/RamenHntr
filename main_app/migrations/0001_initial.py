# Generated by Django 3.1.7 on 2021-04-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ramen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=6)),
                ('description', models.TextField(max_length=380)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
