from django.core.management.base import BaseCommand, CommandError, NoArgsCommand
from django.conf import settings
from django.db.models import get_models


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for model in get_models():
            n = "[%s] - %d objects\n" % (model.__name__, model.objects.count())
            self.stdout.write(n)
            self.stderr.write("Error: ")
            self.stderr.write(n)

