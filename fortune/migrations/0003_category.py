# Generated by Django 3.0.2 on 2020-02-17 11:21

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0002_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
            ],
        ),
    ]