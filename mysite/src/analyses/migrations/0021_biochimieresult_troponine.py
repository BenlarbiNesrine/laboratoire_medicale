# Generated by Django 2.2 on 2020-10-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0020_auto_20200930_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='biochimieresult',
            name='Troponine',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
    ]