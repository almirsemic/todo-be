# Generated by Django 4.1.1 on 2022-09-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['created_date']},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='owner',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='code',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='state',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
