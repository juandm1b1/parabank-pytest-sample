import pytest
from pytest_bdd import scenario, given, when, then
from pytest_bdd import given
from screenpy import See
from screenpy_playwright.actions import Open

from screenpy.resolutions import IsEqualTo
from screenplay.questions.payment_receipt import ThePaymentReceipt
from screenplay.tasks.log_in import LogIn
from screenplay.tasks.pay_bill import PayBill


@pytest.mark.ui
@scenario('../features/bill_payment.feature', 'Successful bill payment')
def test_successful_bill_payment():
    """Successful bill payment scenario binding function."""
    pass
    
@given("the customer has logged into their ParaBank account")
def customer_logged_in(actor):
    """Step: The customer navigates to the app and logs in."""    
    actor.attempts_to(Open("https://parabank.parasoft.com"))    
    actor.attempts_to(LogIn(username="john", password="demo"))

@when('they register a payment for the "Electricity" bill of 150 USD')
def register_bill_payment(actor):
    """Step: The customer performs the bill payment actions."""
    actor.attempts_to(PayBill())

@then("they should see a successful payment confirmation")
def verify_payment_confirmation(actor):
    """Step: The customer verifies the success message and receipt details."""
    actor.should(See.the(ThePaymentReceipt.displayed_for("Tester", "150.25", "19560"), IsEqualTo(True)))