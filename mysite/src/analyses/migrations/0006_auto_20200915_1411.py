# Generated by Django 2.2 on 2020-09-15 13:11

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyses', '0005_coproparasitologyresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coproparasitologyresult',
            old_name='Horodatage_création_de_demande',
            new_name='Horodatage_création_de_resultat',
        ),
        migrations.RenameField(
            model_name='coproparasitologyresult',
            old_name='Nom_Patient',
            new_name='Nom_patient',
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Adresse',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Amaigrissement',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Autre',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Constipation',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Diarrhée',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Douleurs',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Etat_frais',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Examen_Complémentaire',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Kato_Willis',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Macroscopie',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Microscopie',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Nausées',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Ritchie',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Résultat',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Scotch_test',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Symptomes',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='Vomissement',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AddField(
            model_name='coproparasitologyresult',
            name='ballonnement_abdominal',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3),
        ),
        migrations.AlterField(
            model_name='coproparasitologyresult',
            name='Service',
            field=models.CharField(choices=[('Interne', 'Interne'), ('Externe', 'Externe')], default='Interne', max_length=10),
        ),
        migrations.CreateModel(
            name='BilanDurgenceResult',
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