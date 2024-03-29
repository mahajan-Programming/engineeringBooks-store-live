# Generated by Django 3.0.5 on 2020-05-09 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0008_calc'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkShopUniForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books')),
                ('size', models.CharField(default='M', max_length=4)),
                ('CalcOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UniformOwner', to='userRegistration.UserPersonalInfo')),
            ],
        ),
    ]
