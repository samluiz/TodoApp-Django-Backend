# Generated by Django 4.1 on 2022-08-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
