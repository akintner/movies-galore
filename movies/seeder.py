from django_seed import Seed
from faker import Faker

seeder = Seed.seeder()
genres = ['action', 'thriller', 'comedy', 'drama', 'historical drama', 'science fiction', 'romantic comedy', 'horror']

from movies.models import Movie, Actor

seeder.add_entity(Movie, 100, {
    'title': seeder.faker.catch_phrase(),
    'genre': random.choice(genres),
})

seeder.add_entity(Actor, 100, {
  'name': seeder.faker.name(),
  'date_of_birth': seeder.faker.profile.birthdate(),
})

seeder.execute()

from movies.models import Acted_In

seeder.add_entity(Acted_In, 100)

seeder.execute()