# Generated by Django 4.2.6 on 2023-10-25 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='visadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slag', models.CharField(max_length=12, unique=True)),
                ('datetime', models.CharField(max_length=15)),
                ('packegtype', models.CharField(choices=[('FullPackeg', 'Umara'), ('just_visa', 'Visa')], default='FullPackeg', max_length=50)),
                ('airticket', models.CharField(choices=[('sv', 'Sv'), ('qt', 'Qt'), ('gf', 'Gf'), ('bf', 'Bg')], default='sv', max_length=20)),
                ('totalhaji', models.TextField()),
                ('parcost', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='agents', to='agent.agent')),
            ],
        ),
    ]