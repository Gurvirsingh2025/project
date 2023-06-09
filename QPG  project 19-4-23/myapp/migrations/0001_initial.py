# Generated by Django 4.1.7 on 2023-04-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('question_subject', models.CharField(max_length=50)),
                ('question_topic', models.CharField(max_length=50)),
                ('question_type', models.CharField(max_length=20)),
                ('bloom_taxonomy', models.CharField(max_length=20)),
            ],
        ),
    ]
