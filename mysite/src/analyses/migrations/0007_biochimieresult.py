# Generated by Django 2.2 on 2020-09-15 13:56

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyses', '0006_auto_20200915_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiochimieResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_patient', models.CharField(max_length=40)),
                ('Horodatage_création_de_resultat', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('Sexe', models.CharField(choices=[('Femme', 'Femme'), ('Himme', 'Homme')], max_length=10)),
                ('Service', models.CharField(choices=[('Interne', 'Interne'), ('Externe', 'Externe')], max_length=10)),
                ('user', models.ForeignKey(on_delete='None', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
