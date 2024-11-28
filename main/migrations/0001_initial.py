# Generated by Django 3.2.10 on 2024-11-27 17:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='URL')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('background_color', models.CharField(default='#ffffff', help_text='Введите цвет в формате HEX, например, #ffffff.', max_length=7, verbose_name='Цвет фона')),
                ('text_color', models.CharField(default='#000000', help_text='Введите цвет в формате HEX, например, #000000.', max_length=7, verbose_name='Цвет текста')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='news_backgrounds/', verbose_name='Фоновое изображение')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
    ]
