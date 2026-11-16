from screenpy import Actor
from screenpy_playwright.questions import Text
from screenplay.ui.bill_payment_confirmation_page import BillPaymentConfirmationPage


class ThePaymentReceipt():
    """Verify the payment receipt details after a successful bill payment."""

    def __init__(self, expected_payee: str, expected_amount: str, expected_account: str):
        self.expected_payee = expected_payee
        self.expected_amount = expected_amount
        self.expected_account = expected_account

    @classmethod
    def displayed_for(cls, payee: str, amount: str, account: str) -> "ThePaymentReceipt":
        return cls(payee, amount, account)


    def _normalize_amount(self, amount_value) -> float:
        if isinstance(amount_value, str):
            clean_str = amount_value.replace("$", "").replace(",", "").strip()
            return float(clean_str)
        return float(amount_value)
    

    def answered_by(self, the_actor: Actor) -> bool:
        # Get the actual values from the confirmation page
        actual_payee = Text.of_the(BillPaymentConfirmationPage.CONFIRMATION_PAYEE).answered_by(the_actor)
        actual_amount_raw = Text.of_the(BillPaymentConfirmationPage.CONFIRMATION_AMOUNT).answered_by(the_actor)
        actual_account = Text.of_the(BillPaymentConfirmationPage.CONFIRMATION_ACCOUNT).answered_by(the_actor)

        actual_amount_float = self._normalize_amount(actual_amount_raw)
        expected_amount_float = self._normalize_amount(self.expected_amount)

        # Return True if all actual values match the expected values, otherwise False
        return (
            actual_payee == self.expected_payee and
            round(actual_amount_float, 2) == round(expected_amount_float, 2) and
            actual_account == self.expected_account
        )