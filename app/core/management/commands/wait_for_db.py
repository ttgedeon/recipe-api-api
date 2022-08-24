"""
Django command to wait for the database to be available
"""
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    """
    Django command to wait for the database
    """
    
    def handle(self, *args, **kwargs):
        """Encript fo command."""
        self.stdout.write("waiting for database...\n")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.WARNING("Database unavailable, waiting 1 second..."))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
                