# Generated by Django 3.2.5 on 2021-07-29 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('cv_resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=120, null=True)),
                ('skype', models.CharField(blank=True, max_length=120, null=True)),
                ('wechat', models.CharField(blank=True, max_length=120, null=True)),
                ('facebook', models.CharField(blank=True, max_length=120, null=True)),
                ('instagram', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
