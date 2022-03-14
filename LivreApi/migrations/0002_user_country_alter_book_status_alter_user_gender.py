# Generated by Django 4.0.3 on 2022-03-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LivreApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Exchange', 'Exchange'), ('Donate', 'Donate')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
