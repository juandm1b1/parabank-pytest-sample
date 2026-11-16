from screenpy_playwright.target import Target

class BillPaymentServicePage:

    # Bill Payment form
    PAYEE_NAME_FIELD = Target.the("Payee Name field").located_by("input[name='payee.name']")
    ADDRESS_FIELD = Target.the("Adress field").located_by("input[name='payee.address.street']")
    CITY_FIELD = Target.the("City field").located_by("input[name='payee.address.city']")
    STATE_FIELD = Target.the("State field").located_by("input[name='payee.address.state']")
    ZIPCODE_FIELD = Target.the("Zip Code field").located_by("input[name='payee.address.zipCode']")
    PHONE_NUMBER_FIELD = Target.the("Phone # field").located_by("input[name='payee.phoneNumber']")
    ACCOUNT_NUMBER_FIELD = Target.the("Account # field").located_by("input[name='payee.accountNumber']")
    VERIFY_ACCOUNT_FIELD = Target.the("Verify Account # field").located_by("input[name='verifyAccount']")
    AMOUNT_FIELD = Target.the("Amount field").located_by("input[name='amount']")
    FROM_ACCOUNT_DROPDOWN = Target.the("From account # drpdown").located_by("select[name='fromAccountId']")
    SEND_PAYMENT_BUTTON = Target.the("SEND PAYMENT button").get_by_role("button", name="SEND PAYMENT")