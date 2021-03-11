"""
Represents an EscrowCancel transaction on the XRP Ledger.

An EscrowCancel transaction returns escrowed XRP to the sender.

`See EscrowCancel <https://xrpl.org/escrowcancel.html>`_
"""

from dataclasses import dataclass

from xrpl.models.transactions.transaction import REQUIRED, Transaction, TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class EscrowCancel(Transaction):
    """
    Represents an EscrowCancel transaction on the XRP Ledger.

    An EscrowCancel transaction returns escrowed XRP to the sender.

    `See EscrowCancel <https://xrpl.org/escrowcancel.html>`_
    """

    owner: str = REQUIRED
    offer_sequence: int = REQUIRED
    transaction_type: TransactionType = TransactionType.ESCROW_CANCEL
