# Generated by Django 5.0.7 on 2024-07-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='书名')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('publication_date', models.DateField(verbose_name='出版日期')),
            ],
        ),
    ]
