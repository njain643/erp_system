# Generated by Django 2.1.7 on 2019-03-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('dob', models.DateField(max_length=8)),
                ('salary', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
