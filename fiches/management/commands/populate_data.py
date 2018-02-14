import csv

import os
from django.conf import settings
from django.core.management.base import BaseCommand
from fiches.models import Client, Fiche


class Command(BaseCommand):
    help = 'Populate some programs, clients and fiches'

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, "static", "static_dirs", "data",
                               "initial.csv")) as f:
            fiches = csv.reader(f, delimiter=';')
            client_counter = 0
            fiche_counter = 0
            for fiche in fiches:
                client, ccreated = Client.objects.get_or_create(name=fiche[0])
                if ccreated:
                    client_counter += 1

                fiche, fcreated = Fiche.objects.get_or_create(project_title=fiche[1], client=client)
                if fcreated:
                    fiche_counter += 1

        print("{} client créés".format(client_counter))
        print("{} fiches créés".format(fiche_counter))
