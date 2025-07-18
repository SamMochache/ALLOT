# Generated by Django 5.2.4 on 2025-07-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threat_type', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('risk_score', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
