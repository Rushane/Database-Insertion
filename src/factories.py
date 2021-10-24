# For creating test data
from faker import Faker
# from faker.providers import credit_card

import factory
import factory.fuzzy

from factory.django import DjangoModelFactory

import random

from .models import Customer, Account, Creditcard

currencyType = ["JMD", "USD", "CAD", "GBP", "EUR"]
accountTypes = ["Savings", "Joint Account", "Fixed Deposit Account", "Money Market Account"]

# fake = Faker()
# fake.add_provider(credit_card)

class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.firstname, a.lastname).lower())
    phonenumber = factory.fuzzy.FuzzyInteger(9000000000, 9999999999)

class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account
         
    accountnumber = factory.fuzzy.FuzzyInteger(9000000000, 9999999999)
    accountbalance = factory.Faker("pyfloat", left_digits=6, right_digits=2)
    accountcurrency = currencyType[random.randrange(len(currencyType))]
    accountype = accountTypes[random.randrange(len(accountTypes))]
    custid = factory.SubFactory(CustomerFactory)

class AccountFactoryTwo(DjangoModelFactory):
    class Meta:
        model = Account
    
    accountnumber = factory.fuzzy.FuzzyInteger(9000000000, 9999999999)
    accountbalance = factory.Faker("pyfloat", left_digits=6, right_digits=2)
    accountcurrency = currencyType[random.randrange(len(currencyType))]
    accountype = accountTypes[random.randrange(len(accountTypes))]

class CreditCardFactory(DjangoModelFactory):
    class Meta:
        model = Creditcard
         
    cctype = factory.Faker("region", locale='el_GR')
    ccnumber = factory.Sequence(lambda n: 'ccNumber{}'.format(n))
    expirydate = factory.Faker('date')
    custid = factory.SubFactory(CustomerFactory)

class CreditCardFactoryTwo(DjangoModelFactory):
    class Meta:
        model = Creditcard
    
    cctype = factory.Faker("region", locale='el_GR')
    ccnumber = factory.Sequence(lambda n: 'ccNumber{}'.format(n))
    expirydate = factory.Faker('date')