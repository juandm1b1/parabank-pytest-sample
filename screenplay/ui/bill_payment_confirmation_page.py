from screenpy_playwright import Target

class BillPaymentConfirmationPage:
    
    SUCCESS_TITLE = Target.the("success title").get_by_role("heading", name="Bill Payment Complete", level=1)

    # Receipt details
    CONFIRMATION_PAYEE = Target.the("confirmation payee name").located_by("#payeeName")
    CONFIRMATION_AMOUNT = Target.the("confirmation amount").located_by("#amount")
    CONFIRMATION_ACCOUNT = Target.the("confirmation from account").located_by("#fromAccountId")