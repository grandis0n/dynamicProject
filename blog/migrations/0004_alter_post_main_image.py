# Generated by Django 4.2.7 on 2023-11-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(upload_to='static/blog/img', verbose_name='Главное изображение'),
        ),
    ]