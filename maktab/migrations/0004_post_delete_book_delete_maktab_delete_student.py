# Generated by Django 5.1.1 on 2024-10-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maktab', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Maktab',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
