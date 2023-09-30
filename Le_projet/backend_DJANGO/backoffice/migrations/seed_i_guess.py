from django.db import migrations, models
from django.contrib.auth.models import User

def create_user(apps, schema_editor):
    User.objects.create_user(username='test', password='password')


class Migration(migrations.Migration):

    dependencies = [
        # Ajoutez ici les dépendances de migration existantes, le cas échéant
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('en_cours', models.BooleanField(default=True)),
            ],
        ),
    ]

    operations.append(migrations.RunPython(create_user))