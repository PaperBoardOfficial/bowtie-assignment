# Generated by Django 5.0.6 on 2024-06-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_rename_consultation_details_doctor_consultation_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Cantonese', 'Cantonese'), ('Mandarin', 'Mandarin')], default='english', max_length=100),
        ),
    ]
