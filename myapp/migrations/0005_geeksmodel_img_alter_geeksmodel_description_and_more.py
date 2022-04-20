# Generated by Django 4.0.4 on 2022-04-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_geeksmodel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='geeksmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='geeksmodel',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
