# Generated by Django 3.1.2 on 2020-11-07 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ppemsapp', '0002_dailytask_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_of_leave', models.TextField(blank=True, null=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('checked_in', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]