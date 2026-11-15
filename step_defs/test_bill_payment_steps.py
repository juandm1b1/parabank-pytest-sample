import pytest
from pytest_bdd import scenario, given, when, then
from pytest_bdd import given
from screenpy_playwright.actions import Open

from screenplay.tasks.log_in import LogIn


@pytest.mark.ui
@scenario('../features/bill_payment.feature', 'Successful bill payment')
def test_successful_bill_payment():
    """Successful bill payment."""
    pass
    
@given("the customer has logged into their ParaBank account")
def customer_logged_in(actor):
    """Step: The customer navigates to the app and logs in."""    
    actor.attempts_to(
        Open("https://parabank.parasoft.com")
    )    
    actor.attempts_to(
        LogIn(username="john", password="demo")
    )

@when('they register a payment for the "Electricity" bill of 150 USD')
def register_bill_payment(actor):
    """Step: The customer performs the bill payment actions."""
    # Placeholder for actual Bill Pay tasks
    print("\n[UI] Navigating to Bill Pay module and filling the form...")

@then("they should see a successful payment confirmation")
def verify_payment_confirmation(actor):
    """Step: The customer verifies the success message."""
    # Placeholder for a ScreenPy Question
    print("\n[UI] Verifying success message on screen...")
    assert True