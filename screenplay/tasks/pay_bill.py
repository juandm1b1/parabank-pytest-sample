from screenpy import Actor
from screenpy_playwright.actions import Click, Enter, Select
from screenplay.ui.account_services_page import AccountServicesPage
from screenplay.ui.bill_payment_service_page import BillPaymentServicePage


class PayBill:
    def __init__(self):
        self.payee_name = "Tester"
        self.address = "dfcvghjkl"
        self.city= "sdfghj"
        self.state = "dfghjss"
        self.zipcode = "33487"
        self.phone_number = "333999494"
        self.account_number = "22334455"
        self.amount = "150.25"
        self.from_account = "19560"

        
    def perform_as(self, actor : Actor) -> None:
        actor.attempts_to(
            Click.on_the(AccountServicesPage.BILL_PAY_LINK),
            
            Enter.the_text(self.payee_name).into(BillPaymentServicePage.PAYEE_NAME_FIELD),
            Enter.the_text(self.address).into(BillPaymentServicePage.ADDRESS_FIELD),
            Enter.the_text(self.city).into(BillPaymentServicePage.CITY_FIELD),
            Enter.the_text(self.state).into(BillPaymentServicePage.STATE_FIELD),
            Enter.the_text(self.zipcode).into(BillPaymentServicePage.ZIPCODE_FIELD),
            Enter.the_text(self.phone_number).into(BillPaymentServicePage.PHONE_NUMBER_FIELD),
            Enter.the_text(self.account_number).into(BillPaymentServicePage.ACCOUNT_NUMBER_FIELD),
            Enter.the_text(self.account_number).into(BillPaymentServicePage.VERIFY_ACCOUNT_FIELD),
            Enter.the_text(self.amount).into(BillPaymentServicePage.AMOUNT_FIELD),
            Select.the_option(self.from_account).from_the(BillPaymentServicePage.FROM_ACCOUNT_DROPDOWN),
            Click.on_the(BillPaymentServicePage.SEND_PAYMENT_BUTTON)
        )