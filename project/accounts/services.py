from decimal import Decimal

from django.db import transaction

from .models import Account, Transaction


def perform_deposit(user, amount):
    with transaction.atomic():
        account = Account.objects.select_for_update().get(user=user)
        account.balance += Decimal(amount)
        account.save()

        new_transaction = Transaction.objects.create(
            account=account,
            transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT,
            amount=amount
        )

        return new_transaction


def perform_withdrawal(user, amount):
    pass
