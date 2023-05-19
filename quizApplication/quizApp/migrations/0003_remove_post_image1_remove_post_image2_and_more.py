# Generated by Django 4.1.5 on 2023-05-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='Btext',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Quiz Banner'),
        ),
        migrations.AddField(
            model_name='post',
            name='Qtext',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Quiz Açıklması'),
        ),
        migrations.AddField(
            model_name='post',
            name='süre',
            field=models.DurationField(blank=True, null=True, verbose_name='Sınav Süresi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_now',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Quiz Adı'),
        ),
    ]
