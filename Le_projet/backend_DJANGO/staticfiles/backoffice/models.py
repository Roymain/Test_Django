from django.db import models
from faker import Faker

fake = Faker()
# Create your models here.
class Contrat(models.Model):
    nom = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    en_cours = models.BooleanField(default=True)

    @classmethod
    def generate_fake_data(cls, num_contrats):
        for _ in range(num_contrats):
            contrat = cls(
                nom=fake.company(),
                en_cours=fake.boolean(),
                date_debut=fake.date_between(start_date='-1y', end_date='today'),
                date_fin=fake.date_between(start_date='today', end_date='+1y')
            )
            contrat.save()

    def __str__(self):
        return self.nom