# Generated by Django 4.2.10 on 2024-02-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='post.postattachment'),
        ),
    ]