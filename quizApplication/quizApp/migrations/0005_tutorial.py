# Generated by Django 4.1.5 on 2023-05-18 18:27

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_Title', models.CharField(max_length=200)),
                ('tutorial_Body', models.TextField()),
                ('tutorial_Video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'verbose_name_plural': 'Tutorial',
            },
        ),
    ]
