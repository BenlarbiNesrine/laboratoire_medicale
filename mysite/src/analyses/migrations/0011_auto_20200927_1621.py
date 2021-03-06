# Generated by Django 2.2 on 2020-09-27 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0010_auto_20200915_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biochimieminresult',
            old_name='Médecin',
            new_name='medecin',
        ),
        migrations.RemoveField(
            model_name='bilandurgenceresult',
            name='Sexe',
        ),
        migrations.RemoveField(
            model_name='biochimieminresult',
            name='Sexe',
        ),
        migrations.RemoveField(
            model_name='biochimieresult',
            name='Sexe',
        ),
        migrations.RemoveField(
            model_name='coproparasitologyresult',
            name='Sexe',
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Bilirubine_directe',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Bilirubine_total',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='CRP',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Calcium_ionisé',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Créatinine',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Glucose',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='INR',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='K',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='NA',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Urée',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='céphaline_kaolin',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='prothrombine',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='ALB',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='CA',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='Créatinine',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='Glucose',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='K',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='NA',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='Urée',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Acide_urique',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Acide_urique_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Albumine',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Amylase',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Amylase_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Aspect_du_sérum',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Bilirubine_directe',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Bilirubine_indirecte',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Bilirubine_total',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='CK_Femme',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='CK_Homme',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='CK_MB',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Calcium_ionisé',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Calcium_total',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Calcium_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Cholestérol_total',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Clairance',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Créatinine',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Créatinine_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Diurèse',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Fer',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='GOT',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='GPT',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Glucose',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Glucose_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='HDL_Cholestérol',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='LDH',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='LDL_Cholestérol',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Lipase',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Magnésium',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Microalbumine',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='PAL_AMP',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='PAL_DEA',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Phosphore',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Phosphore_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Potasium',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Potasium_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Protéines',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Protéines_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Sodium',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Sodium_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Triglycérides',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Urée',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Urée_ur',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='praticien',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='y_gt_f',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='y_gt_h',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
    ]
