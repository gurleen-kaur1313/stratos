# Generated by Django 3.1.7 on 2021-02-27 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(blank=True, choices=[('Y', 'YOGA'), ('W', 'WEIGHT TRAINING'), ('S', 'SQUATS')], max_length=1, null=True)),
                ('date', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('added', models.DateTimeField(auto_now_add=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
