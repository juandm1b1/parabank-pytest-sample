# ParaBank Automation Framework - Bill Payment Flow

This repository contains a robust QA Automation Framework designed to test the **Bill Payment** flow (simulating a "Payer" experience). The system under test (SUT) is [ParaBank](https://parabank.parasoft.com), a demo banking application.

The project demonstrates the implementation of modern testing practices, including **Data-Driven Testing**, **Contract Testing**, **System Integration Testing (SIT)**, and the **Screenplay Pattern** for UI automation.

## 🛠️ Tech Stack

*   **Language:** Python 3.12
*   **Test Runner:** Pytest `8.3.5`
*   **API & Contract Testing:** Requests `2.32.3`, JSON Schema (`jsonschema` `4.23.0`)
*   **UI Automation:** Playwright `1.50.0`, ScreenPy `4.2.5` & ScreenPy-Playwright `0.0.7` (Screenplay Pattern)
*   **BDD:** Pytest-BDD `8.1.0`
*   **Reporting:** Allure (`allure-pytest` `2.16.2`, `allure-pytest-bdd` `2.16.2`), Pytest-HTML `4.1.1`
*   **Utilities:** Faker `40.54.0` (Dynamic data generation), python-dotenv `1.0.1`

## 📂 Project Architecture

The framework is structured by testing layers to ensure maintainability and execution speed:

```text
├── features/               # Gherkin feature files (UI / E2E)
├── screenplay/             # Screenplay Pattern implementation
│   ├── abilities/          # Actor abilities (e.g., BrowseTheWeb)
│   ├── questions/          # Assertions/Questions (e.g., ThePaymentReceipt)
│   ├── tasks/              # Business tasks (e.g., LogIn, PayBill)
│   └── ui/                 # UI Locators and Page Objects
├── step_defs/              # BDD step definitions for UI
│   ├── conftest.py         # UI-specific fixtures and hooks
│   └── test_bill_payment_steps.py
├── tests/
│   ├── api/                # Isolated API & Contract tests (Fast feedback)
│   ├── sit/                # System Integration Tests (Business flows)
│   ├── ui/                 # UI test configurations
│   ├── payloads/           # External JSON payloads for API requests
│   ├── schemas/            # JSON Schemas for Contract Testing
│   └── conftest.py         # Global fixtures
├── .env                    # Environment variables
├── pytest.ini              # Pytest configuration and custom markers
├── requirements.txt        # Project dependencies
└── README.md


🚀 Execution & Reporting Strategy
Due to a known conflict between allure-pytest and allure-pytest-bdd (both attempt to register the --alluredir command-line option), the test suite must be executed in two isolated phases. By disabling one plugin at a time using the -p no:<plugin_name> flag, we ensure a clean execution while accumulating all results into a single, unified Allure report directory (allure-results).

*Phase 1: API & SIT (Standard Pytest)
Executes API and integration tests. We disable the BDD plugin and clean the Allure results directory to start fresh.

powershell
pytest -m "not ui" -p no:allure_pytest_bdd --alluredir=allure-results --clean-alluredir

*Phase 2: UI / E2E (BDD)
Executes the Screenplay BDD tests. We disable the standard Allure plugin so the BDD plugin can register its options correctly. Note: Do not use --clean-alluredir here to preserve Phase 1 results.

powershell
pytest -m "ui" -p no:allure_pytest --alluredir=allure-results

*Generate the Unified Report
Once both phases are complete, serve the unified Allure report containing API, SIT, and UI results:

powershell
allure serve allure-results