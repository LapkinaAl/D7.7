# Generated by Django 5.0.1 on 2024-01-04 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_author_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.CharField(choices=[('AR', 'Article'), ('NE', 'News')], default='AR', max_length=2),
        ),
    ]
