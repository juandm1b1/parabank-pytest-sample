from screenpy_playwright.target import Target

class AccountServicesPage:
    
    # Access to Bill Pay module
    BILL_PAY_LINK = Target.the("Bill Pay link").located_by('role=link[name="Bill Pay"]')