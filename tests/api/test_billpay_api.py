# API + Contract (POST /billpay)

import pytest
from jsonschema import validate


@pytest.mark.api
@pytest.mark.parametrize("source_account_id, amount_to_pay", [(16119, 100)])  # Bill payment source account:(savings account from customer_id = 12212)
def test_post_billpay(api_client, load_json, source_account_id, amount_to_pay):

    #1. Request to ParaBank billpay endpoint
    url = f"{api_client.base_url}/billpay"
        
    params = {"accountId": source_account_id, "amount": amount_to_pay}

    # Payee:
    body = load_json("payloads/payee_payload.json")    

    response = api_client.post(url, params=params, json=body)

    #2. Check status code
    assert response.status_code == 200, f"Error HTTP: {response.status_code}"

    #3. Parse JSON
    payee_response = response.json()

    #4. Contract validation/testing with jsonschema
    # Definition of how the response must look like
    payee_schema = load_json("schemas/payee_response.json")

    # Validate contract
    validate(instance=payee_response, schema=payee_schema)

    # Validate data integrity (SIT)
    assert payee_response["amount"] == amount_to_pay, "Amount in response doesn't match the requested amount"
    assert payee_response["accountId"] == source_account_id, "Account ID in response doesn't match the source account"
    assert payee_response["payeeName"] is not None, "Payee name should not be null"
    print(f"\n Billpay validated: {payee_response['payeeName']} | Amount: {payee_response['amount']} | Account: {payee_response['accountId']}")