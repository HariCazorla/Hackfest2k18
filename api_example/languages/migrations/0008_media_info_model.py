# Generated by Django 2.1 on 2018-08-31 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0007_client_version_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='MEDIA_INFO_MODEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MEDIA_INFO', models.CharField(max_length=5000)),
            ],
        ),
    ]
