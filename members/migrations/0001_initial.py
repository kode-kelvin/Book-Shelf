# Generated by Django 3.1.1 on 2021-03-06 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField()),
                ('my_picture', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('personal_website', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_account', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_account', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_account', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
