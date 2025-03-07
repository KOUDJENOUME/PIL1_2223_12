# Generated by Django 4.2.2 on 2023-06-21 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id_cours', models.AutoField(primary_key=True, serialize=False)),
                ('nom_cours', models.CharField(max_length=20)),
                ('heures_semaine', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cours',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emploidutemps',
            fields=[
                ('id_emploi', models.AutoField(primary_key=True, serialize=False)),
                ('jour_semaine', models.CharField(max_length=20)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
            ],
            options={
                'db_table': 'emploidutemps',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id_groupe', models.AutoField(primary_key=True, serialize=False)),
                ('nom_groupe', models.CharField(max_length=10)),
                ('description_groupe', models.TextField()),
            ],
            options={
                'db_table': 'groupe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id_profil', models.AutoField(primary_key=True, serialize=False)),
                ('cod_profil', models.CharField(max_length=10)),
                ('nom_profil', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'profil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id_promotion', models.AutoField(primary_key=True, serialize=False)),
                ('nom_promotion', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'promotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id_salle', models.AutoField(primary_key=True, serialize=False)),
                ('nom_salle', models.CharField(max_length=20)),
                ('capacite', models.IntegerField()),
            ],
            options={
                'db_table': 'salle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_users', models.AutoField(primary_key=True, serialize=False)),
                ('numero_matricule', models.CharField(max_length=255, unique=True)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=25)),
                ('adresse_email', models.CharField(max_length=255)),
                ('filiere', models.CharField(max_length=15)),
                ('motpas', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
