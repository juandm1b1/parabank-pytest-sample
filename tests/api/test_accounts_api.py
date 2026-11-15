# API + Contract (GET /accounts)

import pytest
from jsonschema import validate


@pytest.mark.api
@pytest.mark.parametrize("customer_id",[12212])
def test_get_account_details(api_client, load_json, customer_id):    
    
    #1. Request to ParaBank accounts endpoint
    url = f"{api_client.base_url}/customers/{customer_id}/accounts"
    response = api_client.get(url)
    
    #2. Check status code
    assert response.status_code == 200, f"Error HTTP: {response.status_code}"

    #3. Parse JSON
    accounts = response.json()
    assert isinstance(accounts, list), "The response is not a list"
    assert len(accounts) > 0, "Client doesn't have registered accounts"

    #4. Contract validation/testing with jsonschema
    # Definition of how the response must look like
    account_schema = load_json("schemas/accounts_details_response.json")

    # 5. Iterate over all accounts to validate schema and data integrity
    for account in accounts:
        # Validate contract
        validate(instance=account, schema=account_schema)
        print(f"\n Account validated: {account['type']} with balance {account['balance']}")

        # Validate data integrity (SIT)
        assert account["customerId"] == customer_id, (
            f"Account {account['id']} belongs to customer {account['customerId']}, "
            f"but we queried customer {customer_id}"
        )

    print(f"\n {len(accounts)} accounts validated successfully.")