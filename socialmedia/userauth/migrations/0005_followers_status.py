# Generated by Django 5.0.6 on 2024-06-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]