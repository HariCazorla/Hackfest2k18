# Generated by Django 2.1 on 2018-08-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0010_auto_20180831_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOTAL_MODEL_ALL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CM_TOTAL', models.CharField(max_length=50)),
                ('CLIENTS_TOTAL', models.CharField(max_length=50)),
                ('CM_WIN_TOTAL', models.CharField(max_length=50)),
                ('CM_LIN_TOTAL', models.CharField(max_length=50)),
                ('CM_HPUX_TOTAL', models.CharField(max_length=50)),
                ('CM_OTHERS_TOTAL', models.CharField(max_length=50)),
                ('CLIENTS_WIN_TOTAL', models.CharField(max_length=50)),
                ('CLIENTS_HPUX_TOTAL', models.CharField(max_length=50)),
                ('CLIENTS_LIN_TOTAL', models.CharField(max_length=50)),
                ('CLIENTS_VMWARE_TOTAL', models.CharField(max_length=50)),
                ('CLIENTS_OTHERS_TOTAL', models.CharField(max_length=50)),
                ('LIC_EXPRESS', models.CharField(max_length=50)),
                ('LIC_PREMIUM', models.CharField(max_length=50)),
                ('LIC_CAPACITY', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='TOTAL_MODEL',
        ),
    ]
