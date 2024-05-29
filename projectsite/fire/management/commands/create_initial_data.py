from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Incident, FireStation, Locations

class Command(BaseCommand):
    help = 'Create initial data for the application'
    
    def handle(self, *args, **kwargs):
        self.faker = Faker()
        self.create_location(10)
        self.create_firestation(10)
        self.create_incident(10)

    def create_location(self, count):
        for _ in range(count):
            location = Locations.objects.create(
                name=self.faker.company(),
                latitude=self.faker.latitude(),
                longitude=self.faker.longitude(),
                address=self.faker.street_address(),
                city=self.faker.city(),
                country=self.faker.country()
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created location'))

    def create_firestation(self, count):
        for _ in range(count):
            fire_station = FireStation.objects.create(
                name=self.faker.company(),
                latitude=self.faker.latitude(),
                longitude=self.faker.longitude(),
                address=self.faker.street_address(),
                city=self.faker.city(),
                country=self.faker.country()
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created fire station'))

    def create_incident(self, count):
        locations = list(Locations.objects.all())
        severity_choices = [choice[0] for choice in Incident.SEVERITY_CHOICES]

        for _ in range(count):
            incident = Incident.objects.create(
                location=self.faker.random_element(locations),
                date_time=self.faker.date_time_this_year(),
                severity_level=self.faker.random_element(severity_choices),
                description=self.faker.text(max_nb_chars=250)
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created incident with severity'))