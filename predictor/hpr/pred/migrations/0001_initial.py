# Generated by Django 3.1.2 on 2020-10-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predicted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('location', models.IntegerField()),
                ('bhk', models.IntegerField()),
                ('boathroom', models.IntegerField()),
            ],
        ),
    ]