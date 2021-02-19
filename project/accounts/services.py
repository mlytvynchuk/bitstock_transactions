from decimal import Decimal

from .models import Account, Transaction


def perform_deposit(user, amount):
    account = Account.objects.get(user=user)
    account.balance += Decimal(amount)
    account.save()

    transaction = Transaction.objects.create(
        account=account,
        transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT,
        amount=amount
    )

    return transaction


def perform_withdrawal(user, amount):
    pass
