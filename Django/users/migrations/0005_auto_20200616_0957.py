# Generated by Django 3.0.7 on 2020-06-16 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200606_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('comment', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
