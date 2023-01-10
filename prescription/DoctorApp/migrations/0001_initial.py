# Generated by Django 4.1.3 on 2023-01-04 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DoctorName', models.CharField(blank=True, max_length=100)),
                ('medicine', models.CharField(default='none', max_length=100)),
                ('Diseases', models.CharField(default=None, max_length=100)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]