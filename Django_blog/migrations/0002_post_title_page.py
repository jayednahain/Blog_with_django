# Generated by Django 3.1.6 on 2021-02-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_page',
            field=models.CharField(default='GanGBang', max_length=255),
        ),
    ]
