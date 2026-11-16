from faker import Faker
import pytest
from pytest_bdd import parsers, scenario, given, when, then
from pytest_bdd import given
from screenpy import See
from screenpy_playwright.actions import Open

from screenpy.resolutions import IsEqualTo
from screenplay.questions.payment_receipt import ThePaymentReceipt
from screenplay.tasks.log_in import LogIn
from screenplay.tasks.pay_bill import PayBill


@pytest.mark.ui
@pytest.mark.parametrize(
    "payee_name, amount, from_account",
    [
        ("City Power & Light", 150.00, "12900"),
        ("Water Works Inc", 45.50, "17340"),
        ("Internet Provider", 89.99, "17340"),
    ],
)
@scenario('../features/bill_payment.feature', 'Successful bill payment')
def test_successful_bill_payment(payee_name, amount, from_account):
    """Successful bill payment scenario binding function."""
    pass
    
@given("the customer has logged into their ParaBank account")
def customer_logged_in(actor, app_config):
    """Step: The customer navigates to the app and logs in."""    
    actor.attempts_to(Open(app_config["url"]))    
    actor.attempts_to(LogIn.with_credentials(username=app_config["username"], password=app_config["password"]))

@when('they register a payment for the requested bill')
def register_bill_payment(actor, faker: Faker, payee_name, amount, from_account):
    """Step: The customer performs the bill payment actions."""
    fake_payee_data = {
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state(),
        "zipcode": faker.zipcode(),
        "phone_number": faker.phone_number(),
        "account_number": faker.numerify('########')
    } 

    actor.attempts_to(
        PayBill.with_details(
            payee_name=payee_name, 
            amount=str(amount), 
            from_account=from_account,
            fake_data=fake_payee_data
        )
    )

@then("they should see a successful payment confirmation")
def verify_payment_confirmation(actor, payee_name, amount, from_account):
    """Step: The customer verifies the success message and receipt details."""
    actor.should(See.the(ThePaymentReceipt.displayed_for(payee_name, amount, from_account), IsEqualTo(True)))