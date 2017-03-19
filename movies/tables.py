import django_tables2 as tables
from movies.models import Acted_In
import statistics

class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return sum((bound_column.accessor.resolve(row) for row in table.data) / bound_column.length)

class ActorMoviesTable(tables.Table):
    # movies = Acted_In.objects.filter(actor_id=search_id)
    movie_id = tables.Column()
    salary = SummingColumn(footer='Total:')

