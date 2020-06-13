# Generated by Django 2.2.12 on 2020-06-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_data', '0016_auto_20200503_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Markdown for the text of the notice')),
                ('expires', models.DateField()),
            ],
        ),
    ]
