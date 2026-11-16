# SIT (Complete business flow: Verify that a bill payment reduces the source account balance [GET -> POST -> GET])

import pytest

@pytest.mark.sit
@pytest.mark.parametrize("account_id, amount_to_pay", [(16119, 9.0)])  # Bill payment source account:(savings account from customer_id = 12212)
def test_billpay_reduces_account_balance(api_client, load_json, account_id, amount_to_pay):
    
    # 1. GET Initial Balance
    url_account = f"{api_client.base_url}/accounts/{account_id}"
    response_initial = api_client.get(url_account)
    assert response_initial.status_code == 200, f"Failed to get initial balance. Status: {response_initial.status_code}"
    initial_balance = response_initial.json()["balance"]
    
    # 2. POST Bill Payment
    url_billpay = f"{api_client.base_url}/billpay"
    body = load_json("payloads/payee_payload.json")
    params = {"accountId": account_id, "amount": amount_to_pay}
    
    response_post = api_client.post(url_billpay, params=params, json=body)
    assert response_post.status_code == 200, f"Failed to execute bill payment. Status: {response_post.status_code}"
    
    # 3. GET Final Balance
    response_final = api_client.get(url_account)
    assert response_final.status_code == 200, f"Failed to get final balance. Status: {response_final.status_code}"
    final_balance = response_final.json()["balance"]
    
    # 4. Validate Impact (SIT)
    expected_balance = round(initial_balance - amount_to_pay, 2)
    actual_balance = round(final_balance, 2)
    
    assert actual_balance == expected_balance, f"The final balance after bill payment does not match the expected balance. Expected: {expected_balance}, Actual: {actual_balance}"
    print(f"\n SIT 'Verify that a bill payment reduces the source account balance' Passed! Initial Balance: {initial_balance}, Amount Paid: {amount_to_pay}, Final Balance: {final_balance}")