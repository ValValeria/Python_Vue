# Generated by Django 3.1.2 on 2021-12-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='app/static/images')),
                ('link', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('page', models.CharField(choices=[('posts', 'posts'), ('post', 'post'), ('categories', 'categories')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='app/static/images'),
        ),
    ]
