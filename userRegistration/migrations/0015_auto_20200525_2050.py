# Generated by Django 3.0.5 on 2020-05-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0014_auto_20200511_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='Type',
            field=models.CharField(choices=[('MCQ', 'MCQ'), ('Q-paper', 'Q-paper'), ('Notes', 'Notes'), ('Decode', 'Decode'), ('Other', 'Other')], max_length=40),
        ),
    ]
