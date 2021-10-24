from django.db import transaction

from django.core.management.base import BaseCommand

from src.models import Customer, Account, Creditcard
from src.factories import AccountFactoryTwo, CreditCardFactory, CreditCardFactoryTwo, CustomerFactory, AccountFactory
import random

NUM_ACCOUNTS = 50
# i = 1

class Command(BaseCommand):
    help = 'Displays current time'

    # @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(
            "################################# Begin Insertion of Data into DB #################################"
        )
        self.stdout.write("Starting insertion of records into mysql db")

        self.stdout.write("Deleting old data...")
        Customer.objects.all().delete()
        Account.objects.all().delete()
        Creditcard.objects.all().delete()
        self.stdout.write("Creating new data...")

        for _ in range(50):
            CustomerFactory()

        for _ in range(30):
            AccountFactory()
        
        for _ in range(20):
            AccountFactoryTwo()

        for _ in range(30):
            CreditCardFactory()
        
        for _ in range(20):
            CreditCardFactoryTwo()
            
            



