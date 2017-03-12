from django_seed import Seed
from faker import Faker
import random
from movies.models import Movie, Actor, Acted_In

seeder = Seed.seeder()
genres = ['action', 'thriller', 'comedy', 'drama', 'historical drama', 'science fiction', 'romantic comedy', 'horror']

seeder.add_entity(Movie, 100, {
  'title': seeder.faker.catch_phrase(),
  'genre': random.choice(genres),
})

seeder.add_entity(Actor, 100, {
  'name': seeder.faker.name(),
  'date_of_birth': seeder.faker.profile.birthdate(),
})


seeder.add_entity(Acted_In, 100, {
  'movie_id': random.choice(Movie.objects.all()),
  'actor_id': random.choice(Actor.objects.all()),
  'salary': random.randint(10000, 25000000),
})

seeder.execute()