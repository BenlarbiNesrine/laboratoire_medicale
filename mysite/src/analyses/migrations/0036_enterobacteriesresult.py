# Generated by Django 2.2 on 2020-10-03 19:38

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyses', '0035_enterocoqueresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterobacteriesResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_patient', models.CharField(max_length=40)),
                ('Horodatage_création_de_resultat', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Référence', models.CharField(default=None, max_length=200)),
                ('Age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('Service', models.CharField(choices=[('Externe', 'Externe'), ('Interne (COA)', 'Interne (COA)'), ('Interne (POA)', 'Interne (POA)'), ('Interne (COB)', 'Interne (COB)'), ('Interne (Curtillet)', 'Interne (Curtillet)'), ('Interne (Chir Plastique)', 'Interne (Chir Plastique)'), ('Interne (Chir Générale)', 'Interne (Chir Générale)'), ('Interne (CCI)', 'Interne (CCI)'), ('Interne (Chrurgie Maxito faciale)', 'Interne (Chrurgie Maxito faciale)'), ('Interne (Rea Med Rhu)', 'Interne (Rea Med Rhu)'), ('Interne (Med Interne)', 'Interne (Med Interne)'), ('Interne (Néonat)', 'Interne (Néonat)'), ('Interne (MTV)', 'Interne (MTV)'), ('Interne (PU T)', 'Interne (PU T)'), ('Interne (PU Chir)', 'Interne (PU Chir)'), ('Interne (PU MI)', 'Interne (PU MI)')], max_length=10)),
                ('praticien', models.CharField(max_length=40)),
                ('Nature_de_prelèvement', models.CharField(choices=[('Sang', 'Sang'), ('Urine', 'Urine'), ('LCR', 'LCR'), ('Liquide_d_acite', 'Liquide_d_acite'), ('Selles', 'Selles'), ('Pus', 'Pus'), ('Hémoculture', 'Hémoculture')], max_length=10)),
                ('Examen_Directe', models.CharField(max_length=500)),
                ('Germe_isolé', models.CharField(max_length=500)),
                ('Observation', models.CharField(max_length=1000)),
                ('demande_ACIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyses.DemandeDexamen')),
                ('user', models.ForeignKey(on_delete='None', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EnterobacteriesResult',
            },
        ),
    ]
