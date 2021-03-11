import unittest

from xrpl.models.currencies import IssuedCurrency
from xrpl.models.exceptions import XRPLModelException

currency = "BTC"
issuer = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"


class TestUtils(unittest.TestCase):
    def test_kwargs_req(self):
        with self.assertRaises(XRPLModelException):
            IssuedCurrency(currency, issuer)
