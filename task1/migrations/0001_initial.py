# Generated by Django 4.2 on 2024-01-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('review', models.TextField()),
                ('dete_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
