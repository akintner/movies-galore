import django_tables2 as tables
from movies.models import Acted_In

class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return mean(bound_column.accessor.resolve(row) for row in table.data)

class ActorMoviesTable(tables.Table):
    actor_name = tables.Column()
    movies = tables.Column()
    salary = tables.Column(footer='Total:')
    average_salary = SummingColumn()

    def total_salary(self, queryset, is_descending):
        queryset = queryset.annotate(
            title=Acted_In('salary')
        )
