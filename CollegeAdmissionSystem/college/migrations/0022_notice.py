# Generated by Django 3.1.7 on 2021-07-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0021_auto_20210725_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
