# Generated by Django 3.2 on 2021-04-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registracniZnacka', models.CharField(max_length=100)),
                ('znackaATyp', models.CharField(max_length=100)),
                ('pocetNajetychKm', models.IntegerField()),
                ('datumPosledniTK', models.DateField()),
            ],
        ),
    ]
