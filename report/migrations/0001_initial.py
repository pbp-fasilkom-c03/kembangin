# Generated by Django 4.1.2 on 2022-10-30 06:00

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
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(default='0 Tahun', max_length=15)),
                ('height', models.CharField(default='0 cm', max_length=15)),
                ('weight', models.CharField(default='0 kg', max_length=15)),
                ('eat', models.CharField(choices=[('Tidak Baik', 'Tidak baik'), ('Kurang Baik', 'Kurang baik'), ('Cukup Baik', 'Cukup baik'), ('Sangat Baik', 'Sangat baik')], max_length=15)),
                ('drink', models.CharField(choices=[('Tidak Baik', 'Tidak baik'), ('Kurang Baik', 'Kurang baik'), ('Cukup Baik', 'Cukup baik'), ('Sangat Baik', 'Sangat baik')], max_length=15)),
                ('progress', models.TextField(default='-')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
