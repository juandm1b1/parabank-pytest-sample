Feature: Bill Payment
  As a ParaBank customer
  I want to pay my bills online
  So that I can manage my expenses and pay my providers

  Scenario: Successful bill payment
    Given the customer has logged into their ParaBank account
    When they register a payment for the "Electricity" bill of 150 USD
    Then they should see a successful payment confirmation