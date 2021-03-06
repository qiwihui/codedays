# Generated by Django 3.0.2 on 2020-02-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='level',
            new_name='difficulty',
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='kb.Tag'),
        ),
    ]
