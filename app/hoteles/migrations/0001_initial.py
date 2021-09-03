# Generated by Django 3.2.3 on 2021-09-03 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('BARRANQUILLLA', 'Barranquilla'), ('CALI', 'Cali'), ('CARTAGENA', 'Cartagena')], default='BARRANQUILLLA', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('numHabitaciones', models.PositiveIntegerField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciudades', to='hoteles.ciudad')),
            ],
        ),
    ]