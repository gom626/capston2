# Generated by Django 3.1.3 on 2020-12-06 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('people', models.IntegerField(null=True)),
                ('count', models.IntegerField(null=True)),
                ('main_text', models.TextField(null=True)),
                ('Cdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Edate', models.DateTimeField()),
                ('sex', models.BinaryField(null=True)),
                ('create_img', models.ImageField(null=True, upload_to='')),
                ('location', models.CharField(max_length=100, null=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
