from django.core.management.base import BaseCommand
from library.models import Reservation
from django.utils import timezone

class Command(BaseCommand):
    help = 'Cancel expired reservations'

    def handle(self, *args, **kwargs):
        expired_reservations = Reservation.objects.filter(expires_at__lt=timezone.now())
        for reservation in expired_reservations:
            reservation.delete()
            self.stdout.write(self.style.SUCCESS(f'Reservation for {reservation.book.title} expired and cancelled.'))
