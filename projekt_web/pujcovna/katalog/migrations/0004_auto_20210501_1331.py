# Generated by Django 3.2 on 2021-05-01 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0003_vypujcka'),
    ]

    operations = [
        migrations.AddField(
            model_name='vypujcka',
            name='auto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.auto'),
        ),
        migrations.AddField(
            model_name='vypujcka',
            name='zakaznik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.zakaznik'),
        ),
    ]
